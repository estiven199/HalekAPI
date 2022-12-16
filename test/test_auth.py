import os
import pytest
from fastapi import HTTPException
from fastapi.testclient import TestClient
from routes.auth import auth_routes
from utils.functions import validate_token

client = TestClient(auth_routes)


@pytest.mark.parametrize("env_vars", [{"SECRET": "ZQeOwY6pNusL_xnUV_2i2g5F6BhYFaoL4mt9pB5ANw8="}])
def test_generate_token(env_vars):
    os.environ.update(env_vars)
    response = client.post("/generate_token", headers={
        "x-token": "gAAAAABjm11ka8Kh5AgxWxB12Awwh31fe83qGs1TLG5atIHFBBZmabjFufJ3-J1SIRkv2n2i3VwNXgqk3tbfzUznlQOF0xKErA==",
        "x-api-key": "gAAAAABjm4YLsCwWHqZXSNZr6PCEuBSIGChznJjWGWJSBJcwkCBENNM5gi0u791D773Rynov4T10LwwfAfM2cECzOJlkSK8bgehtmmdUAlSBy5a8N3HIl0w=",
        "x-secret-id": "gAAAAABjm120N7cjeEbPm48tI1kcfaxW9fuK2K1O56ylLBiXFyMQkKESnXgsKCmEs2qg3t2ACtmjtnavmg8K_t58PlsKfHZ2azWt5lrpqd0mlKkR-oFLBV4="
    })
    assert response.status_code == 200


def test_generate_token_not_headers_x_token():
    with pytest.raises(HTTPException) as excinfo:
        client.post("/generate_token", headers={
            "x-api-key": "gAAAAABjm4YLsCwWHqZXSNZr6PCEuBSIGChznJjWGWJSBJcwkCBENNM5gi0u791D773Rynov4T10LwwfAfM2cECzOJlkSK8bgehtmmdUAlSBy5a8N3HIl0w=",
            "x-secret-id": "gAAAAABjm120N7cjeEbPm48tI1kcfaxW9fuK2K1O56ylLBiXFyMQkKESnXgsKCmEs2qg3t2ACtmjtnavmg8K_t58PlsKfHZ2azWt5lrpqd0mlKkR-oFLBV4="
        })
    assert excinfo.value.status_code == 400
    assert excinfo.value.detail == "Bad Request"


def test_generate_token_not_headers_x_api_key():
    with pytest.raises(HTTPException) as excinfo:
        client.post("/generate_token", headers={
            "x-token": "gAAAAABjm4YLsCwWHqZXSNZr6PCEuBSIGChznJjWGWJSBJcwkCBENNM5gi0u791D773Rynov4T10LwwfAfM2cECzOJlkSK8bgehtmmdUAlSBy5a8N3HIl0w=",
            "x-secret-id": "gAAAAABjm120N7cjeEbPm48tI1kcfaxW9fuK2K1O56ylLBiXFyMQkKESnXgsKCmEs2qg3t2ACtmjtnavmg8K_t58PlsKfHZ2azWt5lrpqd0mlKkR-oFLBV4="
        })
    assert excinfo.value.status_code == 400
    assert excinfo.value.detail == "Bad Request"


def test_generate_token_not_headers_x_secret_id():
    with pytest.raises(HTTPException) as excinfo:
        client.post("/generate_token", headers={
            "x-token": "gAAAAABjm4YLsCwWHqZXSNZr6PCEuBSIGChznJjWGWJSBJcwkCBENNM5gi0u791D773Rynov4T10LwwfAfM2cECzOJlkSK8bgehtmmdUAlSBy5a8N3HIl0w=",
            "x-api-key": "gAAAAABjm120N7cjeEbPm48tI1kcfaxW9fuK2K1O56ylLBiXFyMQkKESnXgsKCmEs2qg3t2ACtmjtnavmg8K_t58PlsKfHZ2azWt5lrpqd0mlKkR-oFLBV4="
        })
    assert excinfo.value.status_code == 400
    assert excinfo.value.detail == "Bad Request"


def test_validate_token_invalid_token():
    with pytest.raises(HTTPException) as excinfo:
        validate_token(token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ4X3Rva2VuIjoiZ0FBQUFBQmptMTFrYThLaDVBZ3hXeEIxMkF3d2gzMWZlODNxR3MxVExHNWF0SUhGQkJabWFiakZ1ZkozLUoxU0lSa3YybjJpM1Z3TlhncWszdGJmelV6bmxRT0YweEtFckE9PSIsInhfYXBpX2tleSI6ImdBQUFBQUJqbTRZTHNDd1dIcVpYU05acjZQQ0V1QlNJR0Noem5KaldHV0pTQkpjd2tDQkVOTk01Z2kwdTc5MUQ3NzNSeW5vdjRUMTBMd3dmQWZNMmNFQ3pPSmxrU0s4YmdlaHRtbWRVQWxTQnk1YThOM0hJbDB3PSIsInhfc2VjcmV0X2lkIjoiZ0FBQUFBQmptMTIwTjdjamVFYlBtNDh0STFrY2ZheFc5ZnVLMksxTzU2eWxMQmlYRnlNUWtLRVNuWGdzS0NtRXMycWczdDJBQ3RtanRuYXZtZzhLX3Q1OFBsc0tmSFoyYXpXdDVscnBxZDBtbEtrUi1vRkxCVjQ9IiwiZXhwIjoxNjcxMTc3MTc2fQ.THifXaoyNhoDgxqgeTtAI8yAQtgREp43rr41ExfWAu")
    assert excinfo.value.detail == "Invalid token."


def test_validate_expired_token():
    with pytest.raises(HTTPException) as excinfo:
        validate_token(token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ4X3Rva2VuIjoiZ0FBQUFBQmptMTFrYThLaDVBZ3hXeEIxMkF3d2gzMWZlODNxR3MxVExHNWF0SUhGQkJabWFiakZ1ZkozLUoxU0lSa3YybjJpM1Z3TlhncWszdGJmelV6bmxRT0YweEtFckE9PSIsInhfYXBpX2tleSI6ImdBQUFBQUJqbTRZTHNDd1dIcVpYU05acjZQQ0V1QlNJR0Noem5KaldHV0pTQkpjd2tDQkVOTk01Z2kwdTc5MUQ3NzNSeW5vdjRUMTBMd3dmQWZNMmNFQ3pPSmxrU0s4YmdlaHRtbWRVQWxTQnk1YThOM0hJbDB3PSIsInhfc2VjcmV0X2lkIjoiZ0FBQUFBQmptMTIwTjdjamVFYlBtNDh0STFrY2ZheFc5ZnVLMksxTzU2eWxMQmlYRnlNUWtLRVNuWGdzS0NtRXMycWczdDJBQ3RtanRuYXZtZzhLX3Q1OFBsc0tmSFoyYXpXdDVscnBxZDBtbEtrUi1vRkxCVjQ9IiwiZXhwIjoxNjcxMTc3MTc2fQ.THifXaoyNhoDgxqgeTtAI8yAQtgREp43rr41ExfWAuI")
    assert excinfo.value.detail == "You are not authorized to perform this operation"
