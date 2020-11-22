# MSCHF Man Command Documentation:

## General Commands:

### Setting the Prefix:
* `setprefix {prefix}` command accepts one argument, between 1-2 characters to use as the bot command prefix. It's written to the config file to be persistant.

## Administrative Commands:

### Loading, Reloading, and Unloading Cogs:
* `load {cog}` is used to load any cog in the `cogs` directory of the main bot directory. The cogs system allows individual components of the bot to be developed, tested, and activated seperately without needing to take the  bot offline. This command will throw an error when attempting to load a cog that doesn't exist, or a cog that is already loaded.

* `unload {cog}` is used to unload any currently loaded cog. It will throw an error if the cog is already unloaded, or if it doesn't exist.

* `reload {cog}` is used to reload a currently loaded cog without unloading it. This is used for iterative testing with small changes.

* `shutdown` can only be used by the bot owner, to shutdown the bot on the remote server from Discord.

## Ticket System:
The ticket system is specifically made for individual rooms, intended for settling moderation disputes out of the public eye, there is also nothing stopping you from holding private interrogation sessions. Ticket commands are limited to users with the `Manage Channels` Permission. Tickets are viewable by administrators and a "moderator" role by default. You'll have to change the `moderator_role` variable in the `ticketsystem.py` cog if your moderator role isn't named "Moderators"

```py
moderator_role = get(guild.roles, name="Moderators")
```
> *(Default configuration of the `moderator_role` variable, on line 22 of `ticketsystem.py`)*

* `openticket` is used to open a private ticket channel. The channel will be created in the `Tickets` category. Much like an attorney, if you don't have one of these, one will be provided for you. The tickets are numbered on a **semi-persistant** numbering scheme, meaning the ticket numbering will be sequential as long as the bot is running, but will be reset on any bot restarts.

* `closeticket` closes and completely erases all messages in a ticket. This bot does not have the capabilty of making transcripts yet, so if you want to archive your tickets, you'll need to find another way.

* `adduser {user mention}` will give any mentioned user the permissions to see and speak in the ticket the command is used in.
  
* `removeuser {user mention}` will remove the perms from the user, so that they will not be able to see or speak in a ticket.

## Zuckwatch Commands:
Zuckwatch is and was a core part of our server, and thus the bot needed to be able to test passwords from Discord. `zuckpass {password}` or `zp {password}` will use a headless Selenium script to automatically check the password through the actual website.