# TLV record registry
Senders and apps can send custom TLV fields in Lightning payments. Open a [PR](https://github.com/satoshisstream/satoshis.stream/pulls) to add your own fields.


| Key        	| Subject 	| Length (bytes) 	| Description                	| Additional information 	|
|------------	|---------	|----------------	|----------------------------	|------------------------	|
| 696969        | lnpay         | variable              | LNPay wallet destination      |                               |
| 818818        | hive          | variable              | Hive account name             | See below                     |
| 7629168       | tipping       | variable              | Tip note / destination        | Do not use                    |
| 7629169       | podcast       | variable              | JSON encoded metadata         | See below                     |
| 7629171       | tipping       | variable              | Tip note / destination        | See below                     |
| 7629173       | podcast       | variable              | Proposed (WIP) standard       | See below                     |
| 7629175       | podcast       | 64                    | PodcastIndex ID or GUID       |                               |
| 34349334      | chat          | variable              | Chat message                  | Whatsat and more              |
| 34349337      | chat          | ~71                   | Signature                     | See below                     |
| 34349339      | chat          | 33                    | Chat message                  | Whatsat and more              |
| 34349340      | chat          | variable              | Thunder Hub Sending Node Name |                               |
| 34349343      | chat          | 8                     | Timestamp                     | See below                     |
| 34349345      | chat          | variable              | Thunder Hub Content type      | typically "text"              |
| 34349347      | chat          | variable              | Thunder Hub Request type      | typically "text"              |
| 133773310     | podcast       | variable              | JSON encoded data             | See below                     |
| 5482373484    | keysend       | 32                    | Preimage as 32 bytes          |                               |
  




# Additional information

### Field 7629168 [PROBLEMATIC! Use 7629171]
[Tip note](https://github.com/lightningnetwork/lnd/releases/tag/v0.9.0-beta)
Problem is: "a Sending node MUST NOT send evenly-typed TLV records in the extension without prior negotiation." according to spec. So use 7629171!

### Field 7629169
Key-value JSON metadata about the sent payment. Holds data about the timestamp when the payment was sent within the episode.

Example: `{'podcast': 'PODCASTNAME', 'feedID': 1337, 'episode': 'EPISODENAME', 'action': 'boost', 'ts': 33 }`

_It is allowed to send a batch of payments, by sending a **list** of above key-value "blocks" . If you do, consider setting value_msat per block._

Identifying the podcast **required**: use any of `podcast`, `feedID` or `url`. **guid preferred**
* `podcast` (str) Title of the podcast
* `feedID` (int) ID of podcast in PodcastIndex.org
* `url` (int) RSS feed URL of podcast
* `guid` (str) [The `<podcast:guid>` tag](https://github.com/Podcastindex-org/podcast-namespace/blob/main/docs/1.0.md#guid).

Identifying the episode **recommended**: use any of `episode`, `itemID` or `episode_guid`. **itemID preferred**
* `episode` (str) Episode of the podcas
* `itemID` (int) ID of episode in PodcastIndex.org
* `episode_guid` (str) The GUID of the episode

Information about time **recommended**: use any of `time`, `ts`. **ts preferred**
* `time` (str) HH:MM:SS timestamp when the boost/stream was sent WITHIN the episode (playback position)
* `ts` (int) Timestamp when the boost/stream was sent WITHIN the episode (playback position)

Rest of keys:
* `action` **recommended**: (str) "boost" or "stream" 
* `app_name`: **recommended** (str) Name of sending app
* `app_version`: (str) Version of sending app 
* `boost_link`: (str) App specific URL containing route to podcast, episode, and timestamp at time of boost.
* `message` (str) Text message to add to (boost) message
* `name` **recommended** (str) Name for this split in value tag
* `pubkey` (str) Sending node pubkey
* `sender_key` (str) Node key of sending 
* `sender_name` (str) Name of sender (free text, not checked by signatures)
* `sender_id` (str) Static random identifier for users, not displayed by apps, for abuse purposes. Apps can set this per-feed or app-wide. A GUID-like random identifier or a hash works well. Max 32 ascii characters.
* `sig_fields` (str) pipe separated list of fields that are used for signature (example: feedID|itemID|ts|action|sender_key|message)
* `signature` (str) DER-encoded ECDSA signature
* `speed` (str) Speed
* `uuid` (str) Unique UID
* `value_msat`: (int) Number of millisats for this split payment
* `value_msat_total`: (int) TOTAL Number of millisats for the payment (all splits together, before fees. The actual number someone entered in their player, for numerology purposes.)

### Field 7629171
[Tip note](https://github.com/lightningnetwork/lnd/releases/tag/v0.9.0-beta)

### Field 7629173 (PROPOSED)
WIP standard for streaming value sending. JSON metadata about the sent payment.

```json
{
  "version": 1.0,
  "sender": {
    "identifier": "GUID",
    "name": "ListenerX",
    "key": "XYZ",
    "sig": "Signature of pipe-delimited concatenation of base64-encoded identifier + sender_key + destinations + payments JSON",
    "app_name": "Sending application name",
    "app_version": "1.3.3.7"
  },
  "destinations": {
    "1": {
      "type": "podcast",
      "url": "https://example.com/podcast.rss",
      "guid": "EPGUID1111",
      "split_name": "Name from value tag"
    },
    "2": {
      "type": "website",
      "domain": "example.com",
      "uri": "/page.html"
    }
  },
  "payments": [
    { "dest": "1", "value_msat": 1337, "ts": 30, "action": "stream" },
    { "dest": "1", "value_msat": 1337, "ts": 40 },
    { "dest": "1", "value_msat": 1337, "ts": 50 },
    { "dest": "1", "value_msat": 1337, "ts": 60 },
    { "dest": "1", "value_msat": 7777, "ts": 60, "action": "boost", "message": "Great part!" },
    { "dest": "1", "value_msat": 1337, "ts": 70 },
    { "dest": "1", "value_msat": 1337, "ts": 80, "speed": "2" },
    { "dest": "1", "value_msat": 1337, "ts": 90 },
    { "dest": "2", "value_msat": 8888, "message": "Thanks for the site" }
  ]
}
```
* `version` is 1 for now, will change for breaking changes, for example different ways of doing signatures.
* **Sender says something about the person and app sending the payments**
  * All fields are optional; the whole block does not need to be set. 
  * It is suggested to allow the user to choose what identifying information to send.
  * `identifier` is a static value for a sender (listener), up to the application to use a per-feed or podcast-wide identifier. In the future, identifier+signature can be sent as a header, and websites (podcast hosts) can serve different files.
  * `sig` is the signature of some base64-blocks. `sig( concatenate( base64(identifier), "|", base64(sender_key), "|", base64(destinations), "|", base64(payments_json), "|" ) )
  * If signature is set, key must be set
  * `key` is the sending node public key
* **Destinations are value destination identifiers.** Type can be "podcast" or any other type of payment people want to send. Make a PR to this TLV registry to add your own. Developers are free to add their own key/value pairs.
  * Type `podcast`
    * `url` is the URL of the podcast feed. Setting 7629169-like podcast identifiers is also allowed.
    * `guid` is the GUID of the episode
    * `split_name` is the split from the value block (podcaster name et cetera)
  * Type `website`
    * `domain` must be set
    * `uri` is a page identifier
* **Payments are the payments**
  * `dest`. If no `dest` key is given, the first destination is used.
  * `value_msat` must add up to the total of the payment. Processing of payment record MUST stop when the total (processed) value_msat exceeds payment amount.
  * Developers are free to add their own keys.
  * Key registry:
    * `message` is a message for this payment
    * Podcast related:
      * `action` is stream or boost. Assumed to be stream if not set.
      * `ts` is the number of seconds in the ep when this was sent
      * `speed` is the speed that was used when this payment was sent (decimal). Assumed to be 1 if not set.

### Field 7629175
Set to the podcastindex (podcast) ID or GUID for processing

### Field 34349337
See [Whatsat spec](https://github.com/joostjager/whatsat#protocol)
`signature(sender | recipient | timestamp | msg), DER-encoded ECDSA`

### Field 34349343
See [Whatsat spec](https://github.com/joostjager/whatsat#protocol)
Timestamp in nano seconds since unix epoch (big endian encoded)

## Field 133773310
Podcast metadata as sent by Sphinx. Concatenation of JSON encoded data and signature of the JSON string. Suggested to use 7629169.
* feedID: number  
* itemID: number  
* ts: number  
* speed?: string, 
* title?: string  
* text?: string  
* url?: string 
* pubkey?: string  
* type?: string  
* uuid?: string  
* amount?: number 

## Field 818818
Field used by 3speak and other services redirecting Lightning payments to the Hive blockchain via the v4v.app service.
This field is a str containing the Hive Account Name of the recipient, to be used in a customKey, customValue pair.

For example this value block will redirect to the `brianoflondon` Hive account:
```
<podcast:valueRecipient name="Brian of London" address="0396693dee59afd67f178af392990d907d3a9679fa7ce00e806b8e373ff6b70bd8"
  type="node" split="99" customKey="818818" customValue="brianoflondon">
</podcast:valueRecipient>
```

