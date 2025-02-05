/**
 * Main server module for the Person Management API
 * 
 * This module provides a REST API server with the following features:
 * - HTTP server setup and configuration
 * - Static file serving
 * - CORS support
 * - JSON request/response handling
 * - Person search and add functionality
 *
 * Dependencies:
 * - SWI-Prolog HTTP libraries
 * - database.pl (external file containing person database)
 *
 * API Endpoints:
 * GET /api/search - Search persons with optional filters:
 *   - name: String (partial match)
 *   - age: Number (exact match) 
 *   - gender: String (case-insensitive match)
 *
 * POST /api/add - Add new person (PENDING)
 *   - name: String (required)
 *   - age: Number (required)
 *   - gender: String (required)
 *
 * Server Configuration:
 * - Port: 8080
 * - Debug modes enabled for search and add operations
 * - Automatic cleanup on server halt
 *
 */

:- use_module(library(http/thread_httpd)).
:- use_module(library(http/http_dispatch)).
:- use_module(library(http/http_json)).
:- use_module(library(http/http_cors)).
:- use_module(library(http/http_parameters)).
:- use_module(library(http/http_files)).
:- use_module(library(debug)).
:- dynamic product/3.
:- consult('database.pl').

% Enable debugging
:- debug(search).
:- debug(add).

% Server startup
server(Port) :-
    http_server(http_dispatch, [port(Port)]).

% Serve static files
:- http_handler('/', http_reply_from_files('.', []), [prefix]).
:- http_handler('/static/', http_reply_from_files('static', []), [prefix]).

% Define routes with methods
:- http_handler('/api/search', search_handler, [method(get)]).
:- http_handler('/api/add', add_person_handler, [method(post)]).

% Search handler with multiple parameters
   % Extract parameters from request
search_handler(Request) :-
    debug(search, 'Search request received: ~w', [Request]),
    cors_enable,
    http_parameters(Request, [
        name(Name, [optional(true)]),               % Optional name parameter
        age(Price, [optional(true), number]),         % Optional age (must be number)
        gender(Category, [optional(true)])            % Optional gender parameter
    ]),
    debug(search, 'Search parameters - Name: ~w, Price: ~w, Category: ~w', [Name, Price, Category]),
    
     % Search logic using findall
    findall(json{name:N, age:A, gender:G},          % Create JSON objects
        (product(N, A, G),                           % Match person facts
         (var(Name) -> true ; sub_string(N, _, _, _, Name)),                        % Name contains search
         (var(Price) -> true ; A = Price),                                              % Age exact match
         (var(Category) -> true ; downcase_atom(G, GL), downcase_atom(Category, GL))    % Gender match (case insensitive)
        ),
        Results),
    
    debug(search, 'Found results: ~w', [Results]),
    reply_json(json{status: success, results: Results}).



% Add a new predicate to reload the database
reload_database :-
    retractall(product(_, _, _)),
    consult('database.pl').

% Modify the assert_product predicate
assert_product(Name, Price, Category) :-
    open('database.pl', append, Stream),
    format(Stream, '~nproduct(\'~w\', ~w, \'~w\').', [Name, Price, Category]),
    close(Stream),
    reload_database.

% Update the add_person_handler
add_person_handler(Request) :-
    debug(add, 'Add product request received', []),
    cors_enable,
    http_read_json_dict(Request, Data),
    
    % Extract data from the JSON request
    Name = Data.name,
    Price = Data.price,
    Category = Data.category,
    
    % Validate data
    string(Name),
    number(Price),
    string(Category),
    
    % Add the product and reload database
    assert_product(Name, Price, Category),
    
    % Return success response
    reply_json(json{status: success, message: 'Product added successfully'}).

% Initialize server
:- initialization(server(8080)).

% Cleanup on halt
:- at_halt(http_stop_server(8080, [])).