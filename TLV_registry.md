# TLV record registry
Senders and apps can send custom TLV fields in Lightning payments. Open a [PR](https://github.com/satoshisstream/satoshis.stream/pulls) to add your own fields.


| Key        	| Subject 	| Length (bytes) 	| Description                	| Additional information 	|
|------------	|---------	|----------------	|----------------------------	|------------------------	|
| 34349334      | chat          | variable              | Chat message                  | Whatsat and more              |
| 34349337      | chat          | ~71                   | Signature                     | See below                     |
| 34349339      | chat          | 33                    | Chat message                  | Whatsat and more              |
| 34349343      | chat          | 8                     | Timestamp                     | See below                     |
| 5482373484    | keysend       | 32                    | Preimage as 32 bytes          |                               |
| 7629168       | tipping       | variable              | Tip note / destination        | Do not use                    |
| 7629171       | tipping       | variable              | Tip note / destination        | See below                     |
| 7629169       | podcast       | variable              | JSON encoded metadata         | See below                     |



# Additional information
### Chat
See [Whatsat spec](https://github.com/joostjager/whatsat#protocol)
### Field 34349337
`signature(sender | recipient | timestamp | msg), DER-encoded ECDSA`
### Field 34349343
Timestamp in nano seconds since unix epoch (big endian encoded)

### Field 7629168 [PROBLEMATIC! Use 7629171]
[Tip note](https://github.com/lightningnetwork/lnd/releases/tag/v0.9.0-beta)
Problem is: "a Sennding node MUST NOT send evenly-typed TLV records in the extension without prior negotiation." according to spec. So use 7629171!

### Field 7629171
[Tip note](https://github.com/lightningnetwork/lnd/releases/tag/v0.9.0-beta)

### Field 7629169
Key-value JSON metadata about the sent payment. Holds data about the timestamp when the payment was sent within the episode.

Example: `{'podcast': 'PODCASTNAME', 'feedID': 1337, 'episode': 'EPISODENAME', 'action': 'boost', 'ts': 33 }`

_It is allowed to send a batch of payments, by sending a **list** of above key-value "blocks" . If you do, consider setting value_msat per block._

Identifying the podcast: use any of `podcast`, `feedID` or `url`. **feedID preferred**
* `podcast` (str) Title of the podcast
* `feedID` (int) ID of podcast in PodcastIndex.org
* `url` (int) RSS feed URL of podcast

Identifying the spisode: use any of `episode`, `itemID` or `episode_guid`. **itemID preferred**
* `episode` (str) Episode of the podcas
* `itemID` (int) ID of episode in PodcastIndex.org
* `episode_guid` (str) The GUID of the episode

Information about time: use any of `time`, `ts`. **ts preferred**
* `time` (str) HH:MM:SS timestamp when the boost/stream was sent WITHIN the episode (playback position)
* `ts` (int) Timestamp when the boost/stream was sent WITHIN the episode (playback position)

Rest of keys:
* `action` **required**: (str) "boost" or "stream" (required)
* `amount` (int) Amount of sats (optional)
* `app_name`: **recommended** (str) Name of sending app (optional)
* `app_version`: (str) Version of sending app (optional)
* `message` (str) Text message to add to (boost) message
* `name` **recommended** (str) Name for this split in value tag
* `pubkey` (str) Sending node pubkey (optional)
* `sender_key` (str) Node key
* `sig_fields` (str) pipe separated list of fields that are used for signature (example: feedID|itemID|ts|action|sender_key|message)
* `signature` (str) DER-encoded ECDSA signature
* `speed` (str) Speed (optional)
* `uuid` (str) Unique UID (optional)
* `value_msat`: (int) Number of millisats (optional, useful for batches)

