# elektronenhirn
Chatbot that publishes incoming messages

## Deploy using Caprover
[Caprover](https://caprover.com/) is a tool that turns your personal VPS into a Platform as a Service comparable to [dokku](https://dokku.com/) or Heroku.

1. [Get started with Caprover on your VPS and your CLI](https://caprover.com/docs/get-started.html)
2. Create a new app named `elektronenhirn` (or anything else you like) in the Caprover interface and select `Has Persistent Data`
3. Inside the `HTTP Settings` section of the new app enable HTTPS and select `Force HTTPS by redirecting all HTTP traffic to HTTPS`
4. Inside the `App Configs` section of the new app configure the environment variables described in [secrets-example.env](./secrets-example.env)
5. Inside the `App Configs` section add a new persistent directory with the following values
   * `Path in App`: `/srv/opsdroid-matrix-store` (this needs to match the path you entered for the `STORE_PATH` value)
   * `Label`: `elektronenhirn-data` (or anything else you like)
6. On your local machine, clone this repository and `cd` into it `git clone https://github.com/wolfskaempf/elektronenhirn.git && cd elektronenhirn`
7. Run `caprover deploy` and select your server and the app you just created
   * If this command doesn't exist, make sure that you followed [Step 3 of Getting Started with Caprover](https://caprover.com/docs/get-started.html#step-3-install-caprover-cli)
