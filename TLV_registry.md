# TLV record registry
Senders and apps can send custom TLV fields in Lightning payments. Open a [PR](https://github.com/satoshisstream/satoshis.stream/pulls) to add your own fields.

## Keysend (spontaneous payments)
### Field 5482373484
Field holds the preimage as 32 bytes


## Messages (whatsat et cetera)
### Field 34349334
Chat message, variable length

### Field 34349337
Signature of the message, around 71 bytes.

`signature(sender | recipient | timestamp | msg), DER-encoded ECDSA`

### Field 34349339
Sender pubkey, 33 bytes

### Field 34349343
Timestamp in nano seconds since unix epoch (big endian encoded)


## Podcasting (podcasting2.0)
### Field 7629169
Key-value JSON metadata about the sent payment. Holds data about the timestamp when the payment was sent within the episode.

Example: `{'podcast': 'PODCASTNAME', 'episode': 'EPISODENAME', 'action': 'boost', 'time': '00:01:26', 'podcastindex_id': 1337 }`

Keys and values:
```podcast: (str) Title of the podcast (required)
episode: (str) Episode of the podcast (required)
action: (str) "boost" or "stream" (required)
time: (str) HH:MM:SS timestamp when the boost/stream was sent (required)
podcastindex_id: (int) ID of podcast in PodcastIndex.org (recommended)```
