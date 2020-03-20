## Instructions
1. Build the image from dockerfile by running `docker build -t psql:1.0 .`.
2. Run the image `docker run -d --name psql psql:1.0`.
3. (Optional) Verify that postgresql has been set up correctly. Run `docker exec -it psql bash`. This will open up as bash terminal within the container. Enter postgresql cli with `psql -U postgres` and check that the setup was executed correctly.