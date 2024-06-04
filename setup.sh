mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"josh@knoasis.io\"\n\
" > ~/.streamlit/credentials.toml

# Only append the server configuration to avoid overwriting the existing config.toml
echo "\
\n\[server]\n\
headless = true\n\
enableCORS=false\n\
port = \$PORT
" >> ~/.streamlit/config.toml
