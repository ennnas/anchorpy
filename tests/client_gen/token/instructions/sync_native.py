from __future__ import annotations
import typing
from solders.pubkey import Pubkey
from solders.instruction import Instruction, AccountMeta
from ..program_id import PROGRAM_ID


class SyncNativeAccounts(typing.TypedDict):
    account: Pubkey


def sync_native(
    accounts: SyncNativeAccounts,
    program_id: Pubkey = PROGRAM_ID,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) -> Instruction:
    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["account"], is_signer=False, is_writable=True)
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\x9b\xdb$$\xef\x80\x15A"
    encoded_args = b""
    data = identifier + encoded_args
    return Instruction(keys, program_id, data)
