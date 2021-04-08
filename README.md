**This service helps podcasters earn bitcoin.**

You do not need to run your own node, that is all taken care of ("Uncle Jan node")! Just [register the SatoshisStream node](#%EF%B8%8F-use-this-service) and start earning! 

**[Start now!](#-for-podcast-creators)**

_You can always join the [Support group](https://t.me/joinchat/fXmTB7f1e-EyMmRk) for help!_

Features:
* ✅ Receive streaming payments
* ✅ `/claim` your feed in the bot
* ✅ See `/recent` transactions
* ✅ Get `/balance` and `/withdraw` funds
* ✅ Debug feed problems by doing `/checkfeed RSSURL`
* ✅ Get daily updates by default (can be disabled)
* ✅ Get a complete export of data by `/export`ing your payments. You will get an excel file with all payments, withdrawals and more.  
* ✅ **Advanced users:** Enable `/authwithdraw` and auto-send earnings >100 sat to your own node. Why not use your own node? To use the nice statistics (upcoming), for easier switching of destinations, if you don't want to publish your own node key!

![Image showing withdrawals in a scatter plot](https://raw.githubusercontent.com/satoshisstream/satoshis.stream/main/ext/Export.jpg "Export example")


# 🔊 For podcast listeners
Use an app which supports streaming sats to your favorite podcasters. 
* Mobile: [Breez](https://breez.technology/) is an excellent non-custodial Lightning wallet
* Mobile + Desktop: [Sphinx Chat](https://sphinx.chat/) also supports streaming to podcasts
* Desktop/Browser: [podStation](https://podstation.github.io/) browser extension 

# 🎙 For podcast creators
Two ways of getting sats from your listeners. Join the [Support group](https://t.me/joinchat/fXmTB7f1e-EyMmRk) if you need   help!

## ⚡️ Use this service
1. Find your podcast on [podcastindex.org](https://podcastindex.org/). Click the little lightning bolt to go to podcasterwallet.
2. Enter your details on [podcasterwallet](https://podcasterwallet.com/). Then add SatoshisStream as custom node:  03c457fafbc8b91b462ef0b8f61d4fd96577a4b58c18b50e59621fd0f41a8ae1a4
3. Install/open [Telegram](https://t.me/satoshisstreambot), start a conversation with [@StreamingSatsBot](https://t.me/satoshisstreambot) and follow instructions (/claim your feed)

_Withdrawal fee is 3% for the service + 1 % to PodcastIndex for a total of 4%_

## ⚡️ DIY: Do it yourself
1. Set up a Lightning node which supports keysend. [RaspiBlitz](https://github.com/rootzoll/raspiblitz) is an easy FOSS option to set up your own node
2. Set up channels, make sure you have inbound capacity
3. Find your node key and your podcast's RSS URL
4. Manually add a [value block](https://github.com/Podcastindex-org/podcast-namespace/blob/main/value/value.md) **or** enter your details on [podcasterwallet](https://podcasterwallet.com/)
5. Tell your listeners to use an app that supports Podcasting2.0 value
6. Receive sats

# ℹ️ Help for bot users
You can always join the [Support group](https://t.me/joinchat/fXmTB7f1e-EyMmRk) for help! Open [an Issue](https://github.com/satoshisstream/satoshis.stream/issues) if anything is unclear!

## Claiming your feed
1. Find your RSS url, we will use `https://pod.cast/feed.rss` as an example.
2. Type `/claim https://pod.cast/feed.rss`, you will get a **code**. Add this code to a one recent shownotes page. Wait some minutes.
3. Type `/claim https://pod.cast/feed.rss` again and your node is claimed

## Withdrawing funds
1. First claim your feed
2. Then type `/withdraw`, you will see how many sats you can withdraw.
3. Send a Lightning invoice to the bot, the bot will pay your invoice.

# Satoshis.Stream Lightning Node
Node key = 03c457fafbc8b91b462ef0b8f61d4fd96577a4b58c18b50e59621fd0f41a8ae1a4

[Node](https://1ml.com/node/03c457fafbc8b91b462ef0b8f61d4fd96577a4b58c18b50e59621fd0f41a8ae1a4)

# For developers: TLV Registry
Format of payments:
* Find the [TLV registry here](https://github.com/satoshisstream/satoshis.stream/blob/main/TLV_registry.md).
