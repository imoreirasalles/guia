# Catalogue Collections

# Requirements

- Python 3.5 >= (<https://www.python.org>)
- PostgreSQL 9.6 >= (<https://www.postgresql.org>)
- Postgis
- Docker
- Docker-compose


## Local Dev. Enviroment

### Docker

We use Docker to develop our project ( Guia IMS ).

To get started, install docker on your machine. You can head on to [Docker Website](https://www.docker.com/community-edition) and follow through the documentation there for your OS.

For Linux, you can use the convenience-script which can detect most Linux Distros and install it for you.

This is the step-by-step from Docker:

```
$ curl -fsSL get.docker.com -o get-docker.sh
$ sudo sh get-docker.sh

<output truncated>

If you would like to use Docker as a non-root user, you should now consider
adding your user to the "docker" group with something like:

  sudo usermod -aG docker your-user

Remember to log out and back in for this to take effect!

WARNING: Adding a user to the "docker" group grants the ability to run containers which can be used to obtain root privileges on the docker host.

Refer to https://docs.docker.com/engine/security/security/#docker-daemon-attack-surface
for more information.
```

#### docker-compose
You may also need to install to docker-compose which is used to run all the services and run the Django development server. To install go to their [Github repository](https://github.com/docker/compose/releases) and follow the documentation.

After you have all set up run the following command on the project root:

`docker-compose up`

If you need to run any commands on any of the Docker containers use the command:

`docker-compose exec <CONTAINER_NAME> bash` ( without the angle brackets )

#### Rebuild

If necessary, use the `build` option to remake a docker machine from scratch.

```
docker-compose up --build
```

#### Docker inside

If you need inside Access

```
docker-compose exec django bash
```

### Conclusion

You should get familizared with Docker and how to work with it, as it can decrease development time because you don't have to setup a enviroment everytime you change computers or operating systems. Also it makes easier to replicate settings as containers will always be the same.
