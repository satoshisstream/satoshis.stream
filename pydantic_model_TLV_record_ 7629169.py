class KeysendCustomRecord(BaseModel):
    podcast: Optional[str]
    feedID: Optional[int]
    url: Optional[AnyUrl]
    #
    episode: Optional[str]
    itemID: Optional[int]
    episode_guid: Optional[str]
    #
    time: Optional[str]
    ts: Optional[int]
    action: Optional[str]
    app_name: Optional[str]
    app_version: Optional[str]
    boost_link: Optional[str]
    message: Optional[str]
    name: Optional[str]
    pubkey: Optional[str]
    sender_key: Optional[str]
    sender_name: Optional[str]
    sender_id: Optional[str]
    sig_fields: Optional[str]
    signature: Optional[str]
    speed: Optional[str]
    uuid: Optional[str]
    value_msat: Optional[int]
    value_msat_total: Optional[int]



class V4VItem(KeysendCustomRecord):
    r_hash: str
    add_index: int
    value: int
    settle_date: int
    utc_datetime: datetime = None
    localtime: datetime = None
