# TLV record registry
Senders and apps can send custom TLV fields in Lightning payments. Open a [PR](https://github.com/satoshisstream/satoshis.stream/pulls) to add your own fields.


| Key        	| Subject 	| Length (bytes) 	| Description                	| Additional information 	|
|------------	|---------	|----------------	|----------------------------	|------------------------	|
| 7629168       | tipping       | variable              | Tip note / destination        | Do not use                    |
| 7629169       | podcast       | variable              | JSON encoded metadata         | [blip-0010](https://github.com/lightning/blips/blob/master/blip-0010.md)                     |
| 7629171       | tipping       | variable              | Tip note / destination        | [See below](#field-7629171)                     |
| 7629173       | podcast       | variable              | Proposed (WIP) standard       | [See below](#field-7629173-proposed)                     |
| 7629175       | podcast       | 64                    | PodcastIndex ID or GUID       |                               |
| 34349334      | chat          | variable              | Chat message                  | Whatsat and more              |
| 34349337      | chat          | ~71                   | Signature                     | [See below](#field-34349337)                     |
| 34349339      | chat          | 33                    | Send pubkey                   | Whatsat and more              |
| 34349340      | chat          | variable              | Thunder Hub Sending Node Name |                               |
| 34349343      | chat          | 8                     | Timestamp                     | [See below](#field-34349343)                     |
| 34349345      | chat          | variable              | Thunder Hub Content type      | typically "text"              |
| 34349347      | chat          | variable              | Thunder Hub Request type      | typically "text"              |
| 133773310     | podcast       | variable              | JSON encoded data             | [See below](#field-133773310)                     |
| 5482373484    | keysend       | 32                    | Preimage as 32 bytes          |                               |
| 696969        | lnpay         | variable              | LNPay wallet destination      | [See below](#field-696969---lnpay)                     |
| 818818        | hive          | variable              | Hive account name             | [See below](#field-818818---hive)                     |
| 112111100     | lnpay         | variable              | LNPay Wallet ID               | [See below](#field-112111100---lnpay)                     |

# Additional information

### Field 7629168 [PROBLEMATIC! Use 7629171]
[Tip note](https://github.com/lightningnetwork/lnd/releases/tag/v0.9.0-beta)
Problem is: "a Sending node MUST NOT send evenly-typed TLV records in the extension without prior negotiation." according to spec. So use 7629171!

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



# Fields used in customKey / customValue Pairs
## Field 696969 - LNPay
This field allows a payment to be sent to a wallet on the LNPay Site. When used in conjunction with a keyValue given
on that site, LNPay users can receive Keysend Value 4 Value streaming payments.

For any [Wallet on LNPay](https://lnpay.co/) navigate to the [LNPay Dashboard](https://lnpay.co/dashboard/home), find
a wallet and select **details**. In the **Keysend** section there is a box:

```
To KEYSEND to via LND to THIS WALLET run the command below:

lncli sendpayment -d 033868c219bdb51a33560d854d500fe7d3898a1ad9e05dd89d0007e11313588500 -a [NUM_SATOSHIS] --keysend --data 696969=77616c5f6872444873305242454d353736
```

The Value block for this wallet should be:

```xml
<podcast:valueRecipient name="Your Name Here"
  address="033868c219bdb51a33560d854d500fe7d3898a1ad9e05dd89d0007e11313588500"
  type="node" split="99" customKey="696969" customValue="77616c5f6872444873305242454d353736">
</podcast:valueRecipient>
```

## Field 818818 - Hive

Field used by 3speak and other services redirecting Lightning payments to the Hive blockchain via the v4v.app service.
This field is a str containing the Hive Account Name of the recipient, to be used in a customKey, customValue pair.

For example this value block will redirect to the `brianoflondon` Hive account:
```xml
<podcast:valueRecipient name="Brian of London"
  address="0396693dee59afd67f178af392990d907d3a9679fa7ce00e806b8e373ff6b70bd8"
  type="node" split="99" customKey="818818" customValue="brianoflondon">
</podcast:valueRecipient>
```

## Field 112111100 - LNPay

Alternative to `696969` but using the field `Wallet ID` from the `Wallet Access Keys`.

Wallet ID's are text fields looking like `wal_hrDHs0RBEM576`

The Value block for this wallet should be:

```xml
<podcast:valueRecipient name="Your Name Here"
  address="033868c219bdb51a33560d854d500fe7d3898a1ad9e05dd89d0007e11313588500"
  type="node" split="99" customKey="112111100" customValue="wal_hrDHs0RBEM576">
</podcast:valueRecipient>
```
