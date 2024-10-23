 module Main where

suml :: [Int] -> Int 
suml [] =  0
suml (x:xs) = x + suml xs

html_ content = "<html>" <> content <> "</html>"
body_ content = "<body>" <> content <> "</body>"
wrapHtml content = "<html><body>" <> content <> "</body></html>"

main :: IO ()
main = do putStrLn (html_ (body_ "Hello"))
