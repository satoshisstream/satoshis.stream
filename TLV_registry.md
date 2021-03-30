# TLV record registry
Senders and apps can send custom TLV fields in Lightning payments. Open a [PR](https://github.com/satoshisstream/satoshis.stream/pulls) to add your own fields.


| Key        	| Subject 	| Length (bytes) 	| Description                	| Additional information 	|
|------------	|---------	|----------------	|----------------------------	|------------------------	|
| 34349334      | chat          | variable              | Chat message                  | Whatsat and more              |
| 34349337      | chat          | ~71                   | Signature                     | See below                     |
| 34349339      | chat          | 33                    | Chat message                  | Whatsat and more              |
| 34349343      | chat          | 8                     | Timestamp                     | See below                     |
| 5482373484    | keysend       | 32                    | Preimage as 32 bytes          |                               |
| 7629168       | tipping       | variable              | Tip note / destination        | See below                     |
| 7629169       | podcast       | variable              | JSON encoded metadata         | See below                     |



# Additional information
### Chat
See [Whatsat spec](https://github.com/joostjager/whatsat#protocol)
### Field 34349337
`signature(sender | recipient | timestamp | msg), DER-encoded ECDSA`
### Field 34349343
Timestamp in nano seconds since unix epoch (big endian encoded)
### Field 7629168
[Tip note](https://github.com/lightningnetwork/lnd/releases/tag/v0.9.0-beta)
### Field 7629169
Key-value JSON metadata about the sent payment. Holds data about the timestamp when the payment was sent within the episode.

Example: `{'podcast': 'PODCASTNAME', 'feedID': 1337, 'episode': 'EPISODENAME', 'action': 'boost', 'ts': 33 }`

**Keys and values:**

_Some keys are interchangable: [podcast/feedid], [episode/itemID], [time/ts]._

* podcast: `(str) Title of the podcast (required if feedID is not used)`
* **feedID**: `(int) ID of podcast in PodcastIndex.org (required if podcast is not used)`
* episode: `(str) Episode of the podcast (required if itemID is not used)`
* **itemID**: `(int) ID of episode in PodcastIndex.org (required if episode is not used)`
* **action**: `(str) "boost" or "stream" (required)`
* time: `(str) HH:MM:SS timestamp when the boost/stream was sent (required if ts is not used)`
* **ts**: `(int) Seconds in the ep the action was done (required if time is not used)`
* url: `(int) RSS feed URL of podcast (optional)`
* speed: `(str) Speed (optional)`
* pubkey: `(str) Sending node pubkey (optional)`
* uuid: `(str) Unique UID (optional)`
* amount: `(int) Amount of sats (optional)`

