"""
    * GROUP_HANGTIME should be set to the same value as the repeaters in the IPSC network
    * MASTER should be set to True if the rules should be treated as master rules, these rules will then be
        used to determine TG legitimacy and other constraints. Non-Master rule sets do not auto reload, rules from
        those rule sets will only change when the Master reloads the rules.
    * SEND_TGID should be set to True if the rules in this group should be sent to all peers on the network.
        Only one group should have SEND_TGID set to True at any given time.

    * GROUP_VOICE is the list of configured talkgroups.
        * NAME is any name you want, and is used to match reciprocal rules for user-activateion
        * SRC_TS is the source network timeslot
        * SRC_GROUP is the source network talkgroup ID
        * ACTIVE should be set to True if you want the rule active by default, False to be inactive
        * ROUTABLE is a rule that is never "matched", these are mainly used to determine if a talkgroup is
            valid on the network and if any attached radios are ignored.
        * DST_NET is the name of the destination network traffic on the group should be routed to.
        * DST_TS is the destination network timeslot
        * DST_GROUP is the destination network talkgroup ID
        * TO_TYPE is timeout type. If you want to use timers, ON means when it's turned on, it will
            turn off afer the timout period and OFF means it will turn back on after the timout
            period. If you don't want to use timers, set it to 'NONE' or anything else.
        * TIMEOUT is a value in minutes for the timout timer. No, I won't make it 'seconds', so don't
            ask. Timers are performance "expense".
        * ON and OFF are LISTS of Talkgroup IDs used to trigger this rule off and on. Even if you
            only want one (as shown in the ON example), it has to be in list format. None can be
           handled with an empty list, such as " 'ON': [] ".
        * AFFILIATED is a boolean flag that allows traffic on the source talkgroup ID to repeat, regardless of the
            ignore list if the talkgroup has active affiliations.
        * IGNORED is a list of peer IDs that traffic on the source talkgroup ID will not repeat to. A value of
            of '0' in the first element of this list, will indicate the talkgroup is ignored by all peers.
"""

RULES = {
    "Master": {
        "GROUP_HANGTIME": 5,
        "MASTER": True,
        "SEND_TGID": True,
        "GROUP_VOICE": [
            {
                "NAME": "Talkgroup 1",
                "SRC_GROUP": 1,
                "SRC_TS": 1,
                "ACTIVE": True,
                "ROUTABLE": False,
                "DST_NET": "Master",
                "AFFILIATED": False,
                "DST_GROUP": 1,
                "DST_TS": 1,
                "IGNORED": [],
                "TO_TYPE": "NONE",
                "TIMEOUT": 2,
                "ON": [],
                "OFF": [],
            },
            # When DMR/P25 received on this MASTER, Time Slot 1, Talk Group 1; repeat to only other master connected peers
            # This rule is active by default
            # This rule is NOT routable
            {
                "NAME": "Parrot",
                "SRC_GROUP": 9990,
                "SRC_TS": 1,
                "ACTIVE": True,
                "ROUTABLE": True,
                "DST_NET": "Parrot",
                "AFFILIATED": False,
                "DST_GROUP": 9990,
                "DST_TS": 1,
                "IGNORED": [],
                "TO_TYPE": "NONE",
                "TIMEOUT": 2,
                "ON": [],
                "OFF": [],
            },
            # When DMR/P25 received on this MASTER, Time Slot 1, Talk Group 9990; send to PARROT on Time Slot 1 Talk Group 9990
            # This rule is active by default
            # This rule is routable
            {
                "NAME": "Linked System",
                "SRC_GROUP": 1,
                "SRC_TS": 1,
                "ACTIVE": True,
                "ROUTABLE": True,
                "DST_NET": "Repeater-1",
                "AFFILIATED": False,
                "DST_GROUP": 2,
                "DST_TS": 2,
                "IGNORED": [],
                "TO_TYPE": "ON",
                "TIMEOUT": 2,
                "ON": [
                    8,
                ],
                "OFF": [9, 10],
            },
            # When DMR/P25 received on this MASTER, Time Slot 1, Talk Group 1; send to REPEATER-1 on Time Slot 2 Talk Group 2
            # This rule is active by default
            # This rule is routable
            # This rule can be enabled by transmitting on TGID 8
            # This rule can be disabled by transmitting on TGID 9 or 10
            {
                "NAME": "System Wide P25",
                "SRC_GROUP": 65535,
                "SRC_TS": 1,
                "ACTIVE": True,
                "ROUTABLE": False,
                "DST_NET": "Master",
                "AFFILIATED": False,
                "DST_GROUP": 16777215,
                "DST_TS": 1,
                "IGNORED": [],
                "TO_TYPE": "NONE",
                "TIMEOUT": 2,
                "ON": [],
                "OFF": [],
            },
            {
                "NAME": "System Wide DMR TS1",
                "SRC_GROUP": 16777215,
                "SRC_TS": 1,
                "ACTIVE": True,
                "ROUTABLE": False,
                "DST_NET": "Master",
                "AFFILIATED": False,
                "DST_GROUP": 16777215,
                "DST_TS": 1,
                "IGNORED": [],
                "TO_TYPE": "NONE",
                "TIMEOUT": 2,
                "ON": [],
                "OFF": [],
            },
            {
                "NAME": "System Wide DMR TS2",
                "SRC_GROUP": 16777215,
                "SRC_TS": 2,
                "ACTIVE": True,
                "ROUTABLE": False,
                "DST_NET": "Master",
                "AFFILIATED": False,
                "DST_GROUP": 16777215,
                "DST_TS": 2,
                "IGNORED": [],
                "TO_TYPE": "NONE",
                "TIMEOUT": 2,
                "ON": [],
                "OFF": [],
            },
        ],
    },
    "Parrot": {
        "GROUP_HANGTIME": 5,
        "MASTER": False,
        "SEND_TGID": False,
        "GROUP_VOICE": [
            {
                "NAME": "Parrot",
                "SRC_GROUP": 9990,
                "SRC_TS": 1,
                "ACTIVE": True,
                "ROUTABLE": True,
                "DST_NET": "Master",
                "AFFILIATED": False,
                "DST_TS": 1,
                "DST_GROUP": 9990,
                "IGNORED": [],
                "TO_TYPE": "NONE",
                "TIMEOUT": 2,
                "ON": [],
                "OFF": [],
            },
        ],
    },
    "Repeater-1": {
        "GROUP_HANGTIME": 5,
        "MASTER": False,
        "SEND_TGID": False,
        "GROUP_VOICE": [
            {
                "NAME": "Linked System",
                "SRC_GROUP": 1,
                "SRC_TS": 1,
                "ACTIVE": True,
                "ROUTABLE": True,
                "DST_NET": "Repeater-1",
                "AFFILIATED": False,
                "DST_GROUP": 2,
                "DST_TS": 2,
                "IGNORED": [],
                "TO_TYPE": "ON",
                "TIMEOUT": 2,
                "ON": [
                    8,
                ],
                "OFF": [9, 10],
            },
            # When DMRD/P25D received on this CLIENT, Time Slot 1, Talk Group 1; send to MASTER on Time Slot 2 Talk Group 2
            # This rule is active by default
            # This rule is routable
            # This rule can be enabled by transmitting on TGID 8
            # This rule can be disabled by transmitting on TGID 9 or 10
        ],
    },
}

if __name__ == "__main__":
    from pprint import pprint

    pprint(RULES)
