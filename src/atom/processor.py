import staketaxcsv.atom.constants as co
import staketaxcsv.atom.cosmoshub3.processor
import staketaxcsv.common.ibc.api_lcd
import staketaxcsv.common.ibc.handle
import staketaxcsv.common.ibc.processor
from staketaxcsv.atom.config_atom import localconfig
from staketaxcsv.atom.cosmoshub3.make_tx import make_atom_reward_tx
from staketaxcsv.settings_csv import ATOM_NODE


def process_txs(wallet_address, elems, exporter):
    for elem in elems:
        process_tx(wallet_address, elem, exporter)


def _is_legacy_format_cosmoshub3(elem):
    return "value" in elem["tx"]


def process_tx(wallet_address, elem, exporter):
    if _is_legacy_format_cosmoshub3(elem):
        atom.cosmoshub3.processor.process_tx(wallet_address, elem, exporter)
        return

    txinfo = common.ibc.processor.txinfo(
        wallet_address, elem, co.MINTSCAN_LABEL_ATOM, localconfig.ibc_addresses, ATOM_NODE)

    for msginfo in txinfo.msgs:
        result = common.ibc.processor.handle_message(exporter, txinfo, msginfo, localconfig.debug)
        if result:
            continue

        common.ibc.handle.handle_unknown_detect_transfers(exporter, txinfo, msginfo)

    return txinfo
