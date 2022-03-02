**Personal wallets are useful if you want to receive sats, but do not own a podcast.**

# Use cases
* You are a guest on a podcast and want to receive part of a split
* Multiple people (podcast hosts) want to receive their split

# How does it work?
1. Find your personal value. Open Telegram, talk to [@SatohisStreamBot](https://t.me/SatoshisStreamBot) and say /personalwallet . You will see your personal value.
2. This value should end up in a value split. Someone should set key 7771777 to this value (in a split). This can be done on [podcasterwallet](https://podcasterwallet.com) by the feed owner, or manually by feed owners who can edit their feed.
3. If people stream/boost sats, you will get it. Say /personalwallet again to view your balance. Fees apply as usual (4%). The amount you see has the fee subtracted already and can be withdrawn.
4. If you send a Lightning Invoice to the bot of EXACTLY the balance, the bot will the sats to your Lightning wallet!

# Technical specs
* TLV record 7771777 is used. 
* The value is set to the hex encoded telegram user ID (without 0x). 
  * This means people who know your Telegram ID (and know how to translate that to hex) can add a split for you before you even talk to the bot.
  * Payments received for the user before the user talked to the bot are registered and can be claimed by the telegram user
* Because the text is already hex encoded, this (also) means that there is some double encoding going on. That is expected.

# Limitations
No alerts, boostagram messages, exports or insights into payments. Those are for podcast owners only (who claim using the /claim command).

Personal wallets only have a balance which you can withdraw.
