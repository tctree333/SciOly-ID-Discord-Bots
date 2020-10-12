# SciOly-ID-Discord-Bots
A template for creating Discord Bots to study for Science Olympiad ID events, using [sciolyid](https://github.com/tctree333/SciOly-ID).

# Please see the [sciolyid repository](https://github.com/tctree333/SciOly-ID) for the most up-to-date information on creating a Discord ID bot.

## Usage
To setup your own bot, follow these steps:

1. Create a GitHub repository using this template. Click the green `"Use this template"` button above or click [here](https://github.com/tctree333/SciOly-ID-Discord-Bots/generate). Name your new repository something interesting that describes it's purpose.

The following steps contain code editing. While you can edit and create files directly online, it's much easier to use a proper text editor. I recommend using [VSCode](https://code.visualstudio.com/), since there's plenty of extensions that can make your life easier, though there are plenty of other alternatives. You would also have to learn Git to interact with your repository, but there are plenty of tutorials online. GitHub Desktop is also an easy way to interact with GitHub repositories, see [Adding Pictures](#adding-pictures) below.

However, for this particular purpose, editing files online will be sufficient.

1. Open up the `main.py`. This is where you will setup your bot's settings. For examples, see the [examples section](#examples). Setting functions are described in the comments.
2. Now we need to add the lists. Go to `data/lists/` and create a new file called whatever you're IDing. For example, a fossils bot would have a list called `fossils.txt`. If you have categories, create a file for each category. Fill in these files with the lists, one per line.
3. If some items in the list can go by a different name, you can input them in `data/aliases.txt`. Delete everything there and input your aliases one per line, with the name in the other list as the first item.
4. Now, input the links to the wikipedia pages for each item in `data/wikipedia.txt`. You can manually enter them in, making sure the name matches the items in the other list. You can also run `generate_wikipedia.py` in the `scripts` folder a few times to generate the list for you. You will still have to manually go through to ensure the correct link was found. 
5. Register a bot account on the [Discord Developers Portal](https://discordapp.com/developers/applications/). To do so, create a new application. Name your application, then navigate to the `Bot` section, and add a bot. Change your application name if necessary. Update `setup.sh` with your bot token (`Bot` section) and Discord user id. You can also generate your bot invite link. Go to the `OAuth2` section and check `bot` in the `Scopes` section. In the `Bot Permissions` secion, check `Send Messages`, `Embed Links`, and `Attach Files`. Copy the URL generated and update `main.py`.
6. Great! Now we will need to add images. Create a new GitHub repository to host your images [here](https://github.com/new).

This next step will be the most difficult to do online, though it is possible. See the [Adding Pictures](#adding-pictures) section below for more info.

7. You will need to upload at least one picture of each item on the list, but more is definitely reccomended. These will be the pictures you see when using the bot, so more variety and more pictures is better. Get some friends to help out. The repository structure should be `category_name/item_name/image_name`. Images should be smaller than 8MB and in a `.png`, `.jpg`, or `.jpeg` format. You can see examples in the [example section](#examples). To quickly create the directory structure, use the `generate_file_structure.py` script.

Once you have all of this set up, it's now time to run your bot.

8. Clone the code repo locally (if you haven't already) with `git clone CODE_REPO_URL`. Change into that directory with `cd REPO_NAME`.
9. Install a local Redis server by running `chmod +x install-redis.sh && ./install-redis.sh`. Start your Redis server with `redis-server`. [Source](https://redis.io/topics/quickstart)
10. Install any necessary packages with `pip install -r requirements.txt`. You may also want to setup a python virtual environment to avoid package conflicts before installing packages.
11. You are now ready to run the application! Setup the environment with `source setup.sh`. Start the bot with `python3 main.py`.

**Congrats! You just created your own ID Discord bot.** Add your bot to the Discord server of your choice using the invite link generated in step 5.

If there are any issues or you have any questions, let us know in the Bird-ID [Discord support server.](https://discord.gg/xDqYddK)

## Examples

* **Reach for the Stars ID Bot** - [https://github.com/tctree333/Reach-For-The-Stars-Bot]
* **Reach for the Stars ID Bot Images** - [https://github.com/tctree333/Reach-For-The-Stars-Images]
* **Fossils ID Bot** - [https://github.com/tctree333/Fossil-ID]
* **Fossils ID Images** - [https://github.com/tctree333/Fossil-Bot-Images]
* **Bird-ID** - [https://github.com/tctree333/Bird-ID] (doesn't use this template, more advanced)

## Adding Pictures

If you're new to Git and GitHub, an easy way to get started is with GitHub Desktop.
1. Create a GitHub account if you haven't already.
2. Install GitHub Desktop [here](https://desktop.github.com/). Open it.
3. Log in with your GitHub account. Follow the tutorial [here](https://help.github.com/en/desktop/contributing-to-projects/cloning-and-forking-repositories-from-github-desktop) to clone and fork this repository. When you get to step 2, use `"URL"` instad of `GitHub.com` with the url `https://github.com/tctree333/Fossil-Bot-Images.git`. Note the generated `Local Path`. Continue as normal.
4. In your file explorer on your computer, navigate to the generated path. Now you are ready to add images! Drag and drop downloaded images to the appropriate folder, ensuring that images meet the requirements above and deleting `"image.placeholder"` if the folder is not empty. However, if the folder does *not* have images, **do not delete** `"image.placeholder"`.
5. Once you are done adding as many pictures as you want, go back to GitHub Desktop and click `"create a fork"` in the bottom left corner. Fork the repository, and hit `"Commit to master"` in the bottom left corner. Then, hit `"Push Origin"`.
6. Finally, hit `"View on GitHub"` and click `"Pull Request"` near the middle right. Click `"Create Pull Request"`, give it a name and description if you want, and then `"Create Pull Request"`.

Congrats! You just helped add images to the bot! Give me a few days to approve your pull request, and the bot will be using your new images. You don't have to stop here, though. Add more pictures by repeating steps 4-6, though you may have to click `"Fetch Origin"` occasionally to make sure your copy is up to date.

**Thanks for helping out!**
