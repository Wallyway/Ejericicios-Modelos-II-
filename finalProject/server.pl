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
 * POST /api/add - Add new person (commented out in current version):
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
:- consult('database.pl').

% Enable debugging
:- debug(search).
:- debug(add).

% Server startup
server(Port) :-
    http_server(http_dispatch, [port(Port)]).

% Serve static files
:- http_handler('/', http_reply_from_files('.', []), [prefix]).

% Define routes with methods
:- http_handler('/api/search', search_handler, [method(get)]).
:- http_handler('/api/add', add_person_handler, [method(post)]).

% Search handler with multiple parameters
search_handler(Request) :-
    debug(search, 'Search request received: ~w', [Request]),
    cors_enable,
    http_parameters(Request, [
        name(Name, [optional(true)]),
        age(Age, [optional(true), number]),
        gender(Gender, [optional(true)])
    ]),
    debug(search, 'Search parameters - Name: ~w, Age: ~w, Gender: ~w', [Name, Age, Gender]),
    
    findall(json{name:N, age:A, gender:G}, 
        (person(N, A, G),
         (var(Name) -> true ; sub_string(N, _, _, _, Name)),
         (var(Age) -> true ; A = Age),
         (var(Gender) -> true ; downcase_atom(G, GL), downcase_atom(Gender, GL))
        ),
        Results),
    
    debug(search, 'Found results: ~w', [Results]),
    reply_json(json{status: success, results: Results}).

% Add person handler with validation
% add_person_handler(Request) :-
%     debug(add, 'Add request received', []),
%     cors_enable,
%     catch(
%         (   http_read_json(Request, JSONIn),
%             debug(add, 'Received JSON: ~w', [JSONIn]),
            
%             % Extract fields
%             atom_json_term(JSONIn, json([name=Name, age=Age, gender=Gender]), []),
            
%             % Insert person using new predicate
%             insert_person(Name, Age, Gender),
            
%             reply_json(json{status:success, message:'Person added successfully'}, 
%                       [status(201)])
%         ),
%         Error,
%         (   debug(add, 'Error adding person: ~w', [Error]),
%             reply_json(json{status:error, message:'Failed to add person'},
%                       [status(400)])
%         )
%     ).




% Initialize server
:- initialization(server(8080)).

% Cleanup on halt
:- at_halt(http_stop_server(8080, [])).