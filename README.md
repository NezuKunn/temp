# Jpool SIMDs Scanner

## Description
This project offers a Docker container, after installation and launch of which you will be able to access data and statistics on the latest active SIMDs.

## Installation
1. Clone the repository:
    ```bash
   git clone https://github.com/mfactory-lab/simd-vote.git
    ```

2. Install Docker from the official website, here is an example for Linux Ubuntu:
   1. Update packages
        ```bash
       sudo apt update
       sudo apt upgrade
        ```
   2. Install the required packages
        ```bash
       sudo apt install apt-transport-https ca-certificates curl software-properties-common
        ```
   3. Add the official Docker GPG key
        ```bash
       curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
        ```
   4. Set up a Docker repository
        ```bash
       echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
        ```
   5. Install Docker
        ```bash
       sudo apt update
       sudo apt install docker-ce docker-ce-cli containerd.io
        ```
   6. Check the installation
        ```bash
       sudo systemctl status docker
        ```
3. Build and run the container:
   ```bash
   docker-compose up --build
   ```

## Config
In the config.env file you should use your settings before starting the container.

Requests to the RPS are carried out in groups.
1. max_concurrent_requests - Maximum number of requests in one group.
2. time_between_requests - Wait time between request groups.
3. time_between_loads - The time to wait between updates to data in the database.
4. rpc - You need to indicate your RPC.
5. git_key - You need to specify your GitHub key to collect information about SIMDs on your behalf.
6. repo_owner, repo_name, branch, path_git - Constants that should not be changed.
7. server_api_key - Static API key for your application, it can be any, but only with it you will receive a response to the request.
8. server_host - The host of your application, you can change it if necessary and properly configured.
9. server_port - The port of your application, if you change it, you need to specify it in the docker-compose.yml file when forwarding the port from the container.
   
## Testing and use
You only need to use the prepared server API inside the container, below are examples of requests and response values.

1. Swagger page with API preview:
   ```bash
   http://localhost:8000/docs
   ```
   
2. Getting the latest data on a specific SIMD by its number from the database:
   ```bash
   http://localhost:8000/base/get_simd/{simd_id}
   ```
   Instead of **simd_id**, the four-digit SIMD number is written, for example "0228" or "0096".
   
3. Getting the latest data on all SIMDs from the database:
   ```bash
   http://localhost:8000/base/get_all_simds
   ```

4. Request for real data about a specific SIMD by its number from the database:
   ```bash
   http://localhost:8000/now/get_simd/{simd_id}
   ```
   Instead of **simd_id**, the four-digit SIMD number is written, for example "0228" or "0096".

6. Request real data for all SIMDs from the database:
   ```bash
   http://localhost:8000/now/get_all_simds
   ```
