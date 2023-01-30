<p align="center">
    <img src="https://raw.githubusercontent.com/japandotorg/awesome-discord/main/assets/awesome-discord.png" />
</p>

# Awesome Discord ![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)

A curated list of awesome things realted to Discord.

Inspired by [awesome-python](https://github.com/vinta/awesome-python)

## Contents

- [Awesome Discord](#awesome-discord-awesome)
    - [What is Discord?](#what-is-discord)
    - [API Libraries](#api-libraries)
    - [Game SDK & RPC Bindings](#game-sdk--rpc-bindings)
    - [Misc Resources](#misc-resources)
    - [Bots](#bots)
        - [Self Host-able Bots](#self-host-able-bots)
        - [Open Source Public Bots](#open-source-public-bots)
        - [Public Bots](#public-bots)
    - [Bot Lists](#bot-lists)
    - [Clients](#clients)
    - [Subreddits](#subreddits)
    - [Community Guides & Tutorials](#community-guides--tutorials)
    - [Official Resources](#official-resources)
        - [Servers](#servers)
        - [Links](#links)
        - [Community Programs](#community-programs)
        - [Documents](#documents)
    - [Contributing](#contributing)

## What is Discord?

> [Discord](https://discord.com) is a [VoIP](https://en.wikipedia.org/wiki/Voice_over_IP) and [instant messaging](https://en.wikipedia.org/wiki/Instant_messaging) social platform. Users have the ability to communicate with [voice calls](https://en.wikipedia.org/wiki/Voice_over_IP), [video calls](https://en.wikipedia.org/wiki/Videotelephony), [text messaging](https://en.wikipedia.org/wiki/Text_messaging), media and files in private chats or as part of communities called [servers](https://medium.com/@kamalganwani4/what-is-discord-servers-how-to-use-discord-servers-how-to-create-discord-servers-49bfa2676f53). A server is a collection of persistent chat rooms and voice channels which can be accessed via [invite links](https://www.alphr.com/discord-create-invite-link/). Discord runs on [Windows](https://en.wikipedia.org/wiki/Microsoft_Windows), [MacOS](https://en.wikipedia.org/wiki/MacOS), [Android](https://en.wikipedia.org/wiki/Android_(operating_system)), [iOS](https://en.wikipedia.org/wiki/IOS), [iPadOS](https://en.wikipedia.org/wiki/IPadOS), [Linux](https://en.wikipedia.org/wiki/Linux), and in [web browsers](https://en.wikipedia.org/wiki/Web_browser). As of 2021, the service has over 350 million [registered users](https://en.wikipedia.org/wiki/Registered_user) and over 150 million monthly [active users](https://en.wikipedia.org/wiki/Active_users). By 2021 Discord had an estimated value of $7 billion.  There have been as many as 936 million messages sent per day. 

*Source: [Discord - Wikipedia](https://en.wikipedia.org/wiki/Discord)*

## API Libraries

A list of the unofficial Discord API libraries.

* C
    * [Concord](https://github.com/Cogmasters/concord)
    * [Orca](https://github.com/cee-studio/orca)
* C#
    * [Discord.Net](https://github.com/discord-net/Discord.Net)
    * [DisCatSharp](https://github.com/Aiko-IT-Systems/DisCatSharp)
    * [DSharpPlus](https://github.com/DSharpPlus/DSharpPlus)
    * [NetCord](https://github.com/KubaZ2/NetCord)
    * [Remora.Discord](https://github.com/Remora/Remora.Discord)
* C++
    * [D++](https://github.com/brainboxdotcc/DPP)
    * [Discord++](https://github.com/DiscordPP/discordpp)
    * [DiscordCoreAPI](https://github.com/RealTimeChris/DiscordCoreAPI)
    * [Sleepy Discord](https://github.com/yourWaifu/sleepy-discord)
* Clojure
    * [discljord](https://github.com/discljord/discljord)
* Crystal
    * [discordcr](https://github.com/shardlab/discordcr)
* Dart
    * [nyxx](https://github.com/nyxx-discord/nyxx)
* Elixir
    * [coxir](https://github.com/satom99/coxir)
    * [Nostrum](https://github.com/Kraigie/nostrum)
* Go
    * [disgo](https://github.com/DisgoOrg/disgo)
    * [DiscordGo](https://github.com/bwmarrin/discordgo)
    * [Disgord](https://github.com/andersfylling/disgord)
    * [Postcord](https://github.com/Postcord/rest)
    * [arikawa](https://github.com/diamondburned/arikawa)
* Haskell
    * [discord-haskell](https://github.com/aquarial/discord-haskell)
    * [Calamity](https://github.com/simmsb/calamity)
* Java
    * [JDA](https://github.com/DV8FromTheWorld/JDA)
    * [Javacord](https://github.com/Javacord/Javacord)
    * [Discord4J](https://github.com/Discord4J/Discord4J)
    * [discord.jar](https://github.com/discord-jar/discord.jar)
    * [catnip](https://github.com/mewna/catnip)
* Javascript
    * [discord.js](https://github.com/discordjs/discord.js)
    * [Eris](https://github.com/abalabahaha/eris)
    * [Discordeno](https://github.com/discordeno/discordeno)
    * [Harmony](https://github.com/harmonyland/harmony)
    * [droff](https://github.com/tim-smart/droff)
    * [Oceanic](https://github.com/OceanicJS/Oceanic)
    * [SnowTransfer](https://github.com/DasWolke/SnowTransfer)
    * [Tiscord](https://github.com/tiscordlib/tiscord)
    * [Biscuit](https://github.com/oasisjs/biscuit)
    * [Detritus](https://github.com/detritusjs/client)
* Julia
    * [Discord.jl](https://github.com/Xh4H/Discord.jl)
* Kotlin
    * [Kord](https://github.com/kordlib/kord)
* Lua
    * [Discordia](https://github.com/SinisterRectus/Discordia)
* Nim
    * [Dimscord](https://github.com/krisppurg/dimscord)
* Python
    * [discord.py](https://github.com/Rapptz/discord.py)
    * [interactions.py](https://github.com/interactions-py/library)
    * [hikari](https://github.com/hikari-py/hikari)
    * [hata](https://github.com/HuyaneMatsu/hata)
    * [nextcord](https://github.com/nextcord/nextcord)
    * [disnake](https://github.com/DisnakeDev/disnake)
    * [pycord](https://github.com/Pycord-Development/pycord)
    * [NAFF](https://github.com/NAFTeam/NAFF)
    * [enhanced-discord.py](https://github.com/iDevision/enhanced-discord.py)
* PHP
    * [DiscordPHP](https://github.com/discord-php/DiscordPHP)
    * [RestCord](https://github.com/restcord/restcord)
* Rust
    * [Serenity](https://github.com/serenity-rs/serenity)
    * [Twilight](https://github.com/twilight-rs/twilight)
* Ruby
    * [discorb](https://github.com/discorb-lib/discorb)
    * [discordrb](https://github.com/shardlab/discordrb)
* Scala
    * [AckCord](https://github.com/Katrix/AckCord)
    * [Swiftcord](https://github.com/SketchMaster2001/Swiftcord)
    * [SwiftDiscord](https://github.com/nuclearace/SwiftDiscord)

## Game SDK & RPC Bindings

A list of wrapper libraries for the Discord Game SDK & RPC.

* [RPC](https://github.com/discordjs/RPC) - A simple RPC client for Discord written in javascript.
* [discord-sdk](https://github.com/EmbarkStudios/discord-sdk) - An open implementation of the Discord Game SDK in Rust.
* [discord-game-sdk4j](https://github.com/JnCrMx/discord-game-sdk4j) - Java bindings for the Discord Game SDk.
* [discord_game_sdk](https://github.com/ldesgoui/discord_game_sdk) - Rust bindings for the Discord Game SDK.
* [GodotDiscordSDK](https://github.com/LennyPhoenix/GodotDiscordSDK) - A Discord Game SDK wrapper for Godot, written in C.
* [godotcord](https://github.com/Drachenfrucht1/godotcord) - A Discord Game SDK integration for Godot written in C++.
* [node-discord-game](https://github.com/open-unlight/node-discord-game) - The Discord Game SDK for Electron.js.
* [Discord-Game-SDK](https://github.com/HouraiTeahouse/Discord-Game-SDK) - An Unity Package Manager compatible version of the Discord Game SDK.
* [DiscordGameSDK](https://github.com/ProjectBorealis/DiscordGameSDK) - Unoffical Unreal Engine 4 plugin for the Discord Game SDK.
* [Discord.gml](https://github.com/GameMakerDiscord/Discord.gml) - A native extension for Discord Game SDK support in GameMaker: Studio / GMS2.
* [discord-game-sdk-python](https://github.com/NathaanTFM/discord-game-sdk-python) - Discord Game SDK for Python.
* [ClassiCude-RPC](https://github.com/Fam0r/ClassiCube-RPC) - A Discord Game SDK plugin for ClassiCube.
* [discord-rpc-csharp](https://github.com/Lachee/discord-rpc-csharp) - C# custom implementation for Discord Rich Presence.
* [discord-rpc](https://github.com/Vatuu/discord-rpc) - Java wrapper of the Discord-RPC Library for Discord Rich Presence.
* [riche](https://github.com/antsif-a/riche) - A powerful library for interacting with the Discord RPC.

**[Back To Top](#contents)**

## Misc Resources

A list of resources that goes off with the Discord ecosystem.

* [Jishaku](https://github.com/Yucked/Victoria) - A debugging and testing cog for discord.py rewrite bots.
* [Lavalink](https://github.com/freyacodes/Lavalink) - Standalone audio sending node based on Lavaplayer.
* [Wavelink](https://github.com/PythonistaGuild/Wavelink) - A powerful Lavalink library for Discord.py.
* [Lavaplayer](https://github.com/sedmelluq/lavaplayer) - An audio player library for Discord written in Java.
* [PyLav](https://github.com/Drapersniper/PyLav) - A multifunctional Lavalink wrapper library for Discord.py.
* [discord-api-types](https://github.com/sedmelluq/lavaplayer) - Up to date Discord API Typings, versioned by the API version written in typescript.
* [songbird](https://github.com/serenity-rs/songbird) - An async Rust library for the Discord voice API.
* [vscord](https://github.com/leonardssh/vscord) - Fully customizable VS Code extension to get Discord Rich Presnece integration.
* [discord-vscode](https://github.com/iCrawl/discord-vscode) - Update your discord status with a rich presence.
* [discord-irc](https://github.com/reactiflux/discord-irc) - Connects Discord and IRC channels by sending messages back and forth.
* [Sapphire](https://github.com/sapphiredev/framework) - Discord bot framework built on top of discord.js.
* [hikari-lightbulb](https://github.com/tandemdude/hikari-lightbulb) - The official unofficial command handler for the Python discord API wrapper library, Hikari.
* [Victoria](https://github.com/Yucked/Victoria) - Lavalink wrapper for Discord.Net.
* [discord-components](https://github.com/skyra-project/discord-components) - Discord Webc-Components for real looking messages on the web.
* [discord-logo](http://nntin.github.io/discord-logo) - Create your own animated Discord logo and embed it into your website.
* [Permissions Calculator](https://discordapi.com/permissions.html) - Create invite links for bots with specific permissions.
* [Snowstamp](https://snowsta.mp/) - Convert Discord Snowflakes to Timestamp.
* [Discohook](https://discohook.org) - Send webhooks to Discord using a user-friendly UI.
* [Discord Embed Generator](https://cog-creators.github.io/discord-embed-sandbox/) - A sandbox for making discord.py embeds.
* [discord.bio](https://discord.bio/) - Extend your Discord profile with custom profiles.
* [invite.gg](https://invite.gg/) - Create a custom invite for your Discord server and view join stats, etc.
* [bot.discord.io](https://bot.discord.io/) - Create a custom invite link for your Discord bot.
* [PreMiD](https://premid.app/) - PreMiD is a simple, configurable utility that allows you to show what you're doing on the web in your Discord now playing status.
* [Blob Emojis](https://blobs.gg) - Fun and playful Blob Emoji for Discord.
* [BotBlock](https://botblock.org) - Simplify sending your bot's guild count with the BotBlock API.
* [DiscordIPC](https://github.com/jagrosh/DiscordIPC) - Connect locally to the Discord client using IPC for a subset of RPC features like Rich Presence and Activity Join/Spectate.

**[Back To Top](#contents)**

## Bots

A list of Discord Bots.

### Self Host-able Bots

A list of Discord Bots that can be self hosted by anyone & everyone.

* [Red-DiscordBot](https://github.com/Cog-Creators/Red-DiscordBot) - A multi-functional modular Discord bot.
* [Zeppelin](https://github.com/ZeppelinBot/Zeppelin) - Zeppelin is a moderation bot for Discord.
* [modmail](https://github.com/kyb3r/modmail) - A feature rich discord Modmail bot.
* [Discord-MusicBot](https://github.com/SudhanPlayz/Discord-MusicBot) - An advanced discord music bot.
* [gpt-discord-bot](https://github.com/openai/gpt-discord-bot) - An example discord bot that uses the `text-davinci-003` model from openai.
* [discord-tickets](https://github.com/discord-tickets/bot) - A ticket management bot for Discord.
* [aoede](https://github.com/codetheweb/aoede) - A self-hosted Spotify Discord music bot.
* [NadekoBot](https://gitlab.com/Kwoth/nadekobot) - A self-hostable general purpose Discord bot.

**[Back To Top](#contents)**

### Open Source Public Bots

A list of Discord Bots that are open source while serving millions of users.

* [RoboDanny](https://github.com/Rapptz/RoboDanny) - A general purpose Discord bot.
* [Loritta](https://github.com/LorittaBot/Loritta) - A multipurpose Discord bot.
* [GiveawayBot](https://github.com/jagrosh/GiveawayBot) - A Discord giveaway bot.
* [Lawliet](https://github.com/Aninoss/lawliet-bot) - A multipurpose Discord bot.
* [BoobBot](https://github.com/BoobBot/BoobBot) - A Discord NSFW bot.
* [Birthday Bot](https://github.com/scottbucher/BirthdayBot) - A higly customizable birthday Discord bot.
* [Ear Tensifier](https://github.com/Tetracyl/EarTensifier) - A Discord music bot.
* [Logger](https://github.com/curtisf/logger) - A Discord bot for logging different events in your Discord server.
* [ModMail](https://github.com/chamburr/modmail) - A feature-rich Discord bot for easy communication between server staff and users.
* [Countr](https://github.com/countr/countr) - A bot that can manage a counting channel in your guild.
* [Vortex](https://github.com/jagrosh/Vortex) - A moderation Discord bot.
* [Starboard](https://github.com/CircuitSacul/Starboard-3) A reliable and feature-rich starboard bot.
* [Skyra](https://github.com/skyra-project/skyra) - A configurable Discord bot with fun commands, moderation, and much more.
* [poketwo](https://github.com/poketwo/poketwo) - A pokemon discord bot.
* [Discord-OwO-Bot](https://github.com/ChristopherBThai/Discord-OwO-Bot) - A Discord bot that will keep track of your OwO.

**[Back To Top](#contents)**

### Public Bots

A list of invitable Discord bots.

* [Dyno](https://dyno.gg/) - A general purpose discord bot.
* [DankMemer](https://dankmemer.lol/) - A currency focused Discord bot.
* [Karuta](https://karuta.com/) - A collectible anime card game Discord bot.
* [Mudae](https://top.gg/bot/432610292342587392) - A collectible anime/game card Discord bot.
* [EPIC RPG](https://top.gg/bot/555955826880413696) - A simple RPG game Discord bot with dungeaons, armors, swords, PvP, leaderboards, gambling and memes.
* [Tatsu](https://tatsu.gg) - A cute leveling Discord bot.
* [Mimu](https://mimu.bot) - A cuter aesthetic per-server money economy system Discord bot.
* [Virtual Fisher](https://virtualfisher.com) - Virtual Fisher is a discord game bot focused on fishing.
* [MELON](https://melonbot.io) - An all-in-one multipurpose Discord bot.

**[Back To Top](#contents)**

## Bot Lists

A list of public discord bot lists.

* [Infinity Bots](https://infinitybots.gg/)
* [Bladelist](https://bladelist.gg)
* [top.gg](https://top.gg/)
* [Bots For Discord](https://botsfordiscord.com/)
* [Bots On Discord](https://bots.ondiscord.xyz/)
* [Discord Bots](https://discord.bots.gg/)
* [Discord Bot List](https://discordbotlist.com/)
* [Discord Bots App](https://discordbots.app/)
* [Discord Extreme List](https://discordextremelist.xyz/)

**[Back To Top](#contents)**

## Clients

A list of official and unofficial Discord clients.

> **Warning**
> Use of "client mods" are against the Discord TOS - use at your own risk.

> **Note**
> All the official clients here redirect to the Windows installer only.

* [Discord](https://discord.com/api/download/stable?platform=win) - The official Discord Client application.
* [Discord PTB](https://discord.com/api/download/ptb?platform=win) - The official public test build client.
* [Discord Canary](https://discord.com/api/download/canary?platform=win) - The official canary build client.
* [Powercord](https://powercord.dev/) - A lightweight Discord client mod focused on simplicity and performance.
* [Replugged](https://github.com/replugged-org) - A maintained fork of Powercord - a lightweight Discord client mod focused on simplicity and performance.
* [BetterDiscord](https://betterdiscord.app/) - BetterDiscord extends the functionality of DiscordApp by enchancing it with new features.
* [Demoncord](https://git.ruthenic.com/Demon/demoncord-rewrite) - A Discord client mod by satanists for satanits.
* [Kernal](https://github.com/kernel-mod) - A super small and fast Electron client mod with the most capability.
* [GooseMod](https://goosemod.com/) - GooseMod is a new, store-driven Discord mod. Runs on web browsers too.
* [Discord-Lite](https://github.com/therealcyber71/Discord-Lite) - A light-weight Discord client written in Python.
* [WebCord](https://github.com/SpacingBat3/WebCord) - A Discord and Fosscord API-less client made with Electron.
* [Discord-Sandbox](https://github.com/khlam/discord-sandboxed) - Open-source Sandbox Discord client for the privacy-minded.
* [LemonCord](https://github.com/japandotorg/LemonCord) - A fast & light weight Discord client written in Rust.

**[Back To Top](#contents)**

## Subreddits

A list of community subreddits for Discord.

* [/r/discordapp](https://www.reddit.com/r/discordapp) - The official Discord subreddit.
* [/r/discord_bots](https://www.reddit.com/r/Discord_Bots) - A subreddit dedicated to discord bots.
* [/r/discordservers](https://www.reddit.com/r/discordservers) - A subreddit dedicated to discord servers.

**[Back To Top](#contents)**

## Community Guides & Tutorials

* [An Idiot's Guide](https://anidiots.guide/) - A guide that makes the best effort on attempting at humanizing the use of the Discord.js library.
* [Discord Guide](https://discordguide.github.io/#/index) - A guide that provides content, and support for how to utilize Discord.
* [Server Advertisement Guide](https://austinhuang.me/advertising.html) - A helping guide to advertise Discord servers or bots.

**[Back To Top](#contents)**

## Official Resources

A list of official resources provided by Discord.

### Servers

* [Discord Townhall](https://discord.gg/discord-townhall) - The official discord community server.
* [Discord Developers](https://discord.gg/discord-developers) - The official place to discuss Discord's API and SDKs with the community developers and Discord staffs.
* [Discord API](https://discord.gg/discord-api) - The official Discord server for support related to all the official unofficial API libraries.
* [Discord Games Lab](https://discord.gg/discordgameslab) - The official server for Discord's Games Lab.

**[Back To Top](#contents)**

### Links

* [Discord Terms of Service](https://dis.gd/terms) - Discord's Terms of Service is a policy you must agree to when using it's platform.
* [Discord Privacy Policy](https://discord.com/privacy) - Discord's privacy policy regarding users' information.
* [Discord Community Guidelines](https://dis.gd/guidelines) - Discord's Community Guidelies clarify restrictions and limitations within it's platform.
* [Discord Blog](https://blog.discordapp.com/) - Discord's Blog, where you can find change logs and more.
* [Discord Documentation](https://discordapp.com/developers) - Documentation for using the Discord API.
* [Discord Nitro](https://discordapp.com/nitro) - Support Discord's development and get some sweet perks.
* [Discord Help Center](https://support.discord.com/) - An official Discord navigation page full with useful support articles on every topic.
* [Discord Safety Center](https://discord.com/safety) - A page that provides information about internet privacy & information for parents and educators about how to protect themselves/their children online.
* [Discord Status](https://status.discordapp.com/) - Check Discord's current status, and get to know about any planned maintenance.
* [Discord YouTube Channel](https://www.youtube.com/c/discord) - The official Discord channel on YouTube.
* [Discord Client Downloads](https://discord.com/download) - All official downloadable Discord clients.
* [Discord Branding Page](https://discord.com/branding) - The official branding page for Discord.
* [Discord Security Bug Bounties](https://discord.com/security) - The place to submit security vulnerabilities within Discord.

**[Back To Top](#contents)**

### Community Programs

* [HypeSquad](https://discordapp.com/hypesquad) - Join the HypeSquad and let Discord support your gaming community.
* [Partners](https://discordapp.com/partners) - Join the Discord fam and get partner-only tools to make you stand out.
* [Verification](https://discordapp.com/verification) - Verify your server so people know where to find their favorites artists, esports organizations, and game studios.

**[Back To Top](#contents)**

### Documents

* [Slides](https://docs.google.com/presentation/d/18QQyl0WhTOdYt0F0mBPQf2AusBPF7HqP8e39zjEwKsc/edit#slide=id.g130c86c984d_0_12) & [Audio](https://cdn.discordapp.com/attachments/960960145800704030/982392876254232667/DAC_AuditingYourServer_ExperimentalContent.mp3) - A Discord presentation and audio regarding server audits.
* [Audio](https://dis.gd/RadioDiscord_Accessibility) & [Transcript](https://dis.gd/RadioDiscordAccessibilityTranscript) - A Discord interview about accessibility with a Discord employee. from the accessibility team.
* [Audio](https://dis.gd/Radio-Discord-Forums-Beta) & [Transcript](https://dis.gd/Radio-Discord-Forums-Beta-Transcript) - The Discord community team talks about a new feature in testing: forums. 

**[Back To Top](#contents)**

## Contributing

If you would like to contrtibute, please read [CONTRIBUTING.md](/CONTRIBUTING.md) first. It contains all the necessary information to help keep things organized. Just click [README.md](https://github.com/japandotorg/awesome-discord/edit/main/README.md) to submit a [pull request](https://github.com/japandotorg/awesome-discord/edit/main/README.md). IF this list is not complete, you can [contribute](https://github.com/japandotorg/awesome-discord/edit/main/README.md) to make it so. Here is a great video tutorial to learn how to [contribute on Github](https://egghead.io/lessons/javascript-identifying-how-to-contribute-to-an-open-source-project-on-github)

> Please, help organize these resources so that they are easy to find and understandable for newcomers. See how to [Contribute](/CONTRIBUTING.md) for tips!

***If you see a link here that is not (any longer) a good fit, you can fix it by submitting a [pull request](https://github.com/japandotorg/awesome-discord/edit/main/README.md) to improve this file. Thank you!***

The creators and maintainers of this list do not recieve any form of payment to accept a change made by any contributor. This page is not an official Discord product in any way. It is a list of links to projects and is maintained by volunteering contributors. Everybody is welcome to contribute. The goal of this repo is to index all-things-discord, not to advertise for profit.

[![Contributors][contributors-image]][contributors-link]

[contributors-image]: https://contrib.rocks/image?repo=japandotorg/awesome-discord
[contributors-link]: https://github.com/japandotorg/awesome-discord/graphs/contributors

**[Back To Top](#contents)**
