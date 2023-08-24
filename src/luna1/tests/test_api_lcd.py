import json
import os
import unittest
from unittest.mock import patch
from staketaxcsv.luna1.api_lcd import LcdAPI
from staketaxcsv.common.ibc.api_lcd_cosmwasm import CosmWasmLcdAPI

def _get_fixture_file_content(name):
    with open(f"{os.path.dirname(os.path.realpath(__file__))}/fixtures/{name}") as f:
        return json.loads(f.read())

class APILCDTest(unittest.TestCase):
    def test_contract_info(self):
        contract_history = _get_fixture_file_content("cosmwasm_contract_history.json")
        contract_data =  _get_fixture_file_content("cosmwasm_contract.json")
        with patch.object(CosmWasmLcdAPI, "contract_history", return_value=contract_history):
            with patch.object(CosmWasmLcdAPI, "contract", return_value=contract_data):
                contract_wasm = LcdAPI.contract_info_from_cosmwasm("blah")

        assert contract_wasm ["code_id"] == "4"
        assert contract_wasm["msg"] == contract_wasm["init_msg"]
        assert contract_wasm["result"] == contract_wasm["contract_info"]

    def test_contract_info_from_cosmwasm(self):
        contract_history = _get_fixture_file_content("cosmwasm_contract_history.json")
        contract_data =  _get_fixture_file_content("cosmwasm_contract.json")
        with patch.object(CosmWasmLcdAPI, "contract_history", return_value=contract_history):
            with patch.object(CosmWasmLcdAPI, "contract", return_value=contract_data):
                contract_wasm = LcdAPI.contract_info_from_cosmwasm("blah")

        assert contract_wasm ["code_id"] == "4"
        assert contract_wasm["updated"] == {
            "block_height": "13215800",
            "tx_index": "0"
        }
        assert contract_wasm["msg"] == {
            "asset_infos": [
            {
                "token": {
                "contract_addr": "terra1kc87mu460fwkqte29rquh4hc20m54fxwtsx7gp"
                }
            },
            {
                "native_token": {
                "denom": "uluna"
                }
            }
            ],
            "init_hook": {
            "contract_addr": "terra1ulgw0td86nvs4wtpsc80thv6xelk76ut7a7apj",
            "msg": "eyJyZWdpc3RlciI6eyJhc3NldF9pbmZvcyI6W3sidG9rZW4iOnsiY29udHJhY3RfYWRkciI6InRlcnJhMWtjODdtdTQ2MGZ3a3F0ZTI5cnF1aDRoYzIwbTU0Znh3dHN4N2dwIn19LHsibmF0aXZlX3Rva2VuIjp7ImRlbm9tIjoidWx1bmEifX1dfX0="
            },
            "token_code_id": 3
        }
        assert contract_wasm["result"] == {
            "code_id": "7604",
            "creator": "terra1ulgw0td86nvs4wtpsc80thv6xelk76ut7a7apj",
            "admin": "terra1ulgw0td86nvs4wtpsc80thv6xelk76ut7a7apj",
            "label": "terra1jxazgm67et0ce260kvrpfv50acuushpjsz2y0p",
            "created": {
                "block_height": "13215800",
                "tx_index": "0"
            },
            "ibc_port_id": ""
        }

