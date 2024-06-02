mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"you@example.com\"\n\
" > ~/.streamlit/credentials.toml

# Only append the server configuration to avoid overwriting the existing config.toml
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = \$PORT\n\
" >> ~/.streamlit/config.toml
