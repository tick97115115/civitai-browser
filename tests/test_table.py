from typing import List
from sqlmodel import create_engine, Session, SQLModel, select
from api.v1.db.civitai_table import CivitAI_Model, CivitAI_ModelVersion, CivitAI_Tag
from civitai_api.v1.models.modelId_endpoint import ModelId_Response
import pytest

@pytest.fixture
def civitai_model_data_0():
    import json
    from os.path import dirname, join
    data = json.loads(join(dirname(__file__), 'data.json'))
    data = ModelId_Response(**data)
    return data

@pytest.fixture
def civitai_model_data_1():
    return {
    "id": 11821,
    "name": "VSK-94 | Girls' Frontline",
    "description": "<p>VSK-94 from Girls' Frontline<br />Trained on 4 outfits<br /></p><p><strong>Normal</strong><br />vsknormal, white shirt, blue skirt, pantyhose, patch, snowflake hair ornament, bowtie, short hair, black jacket,pouches,<br /><br /><strong>Normal Jacket Removed</strong><br />vsknormal, white shirt, blue skirt, pantyhose, snowflake hair ornament, bowtie, short hair<br /><br /><strong>Dress</strong><br />vskdress, black dress, jewelry, snowflake hair ornament, short hair, navel<br /><br /><strong>Christmas Lingerie </strong><br />vskchristmas, short hair, blue bikini, fur trim, animal ears,red cape, headband, thighhighs,<br /><br /><strong>Inpainting keyword: </strong>VSKface<br /><br />Recommend 0.8-1 Strength<br /><br />Join my discord for exclusive LoRAs!<br /><a target=\"_blank\" rel=\"ugc\" href=\"https://discord.gg/B89NRj8Uqh If\">https://discord.gg/B89NRj8Uqh<br /></a>If you've enjoyed my models, consider leaving a tip.<br /><a target=\"_blank\" rel=\"ugc\" href=\"https://ko-fi.com/leontalon Commission\">https://ko-fi.com/leontalon<br /></a>Commission requests are also open<br /><a target=\"_blank\" rel=\"ugc\" href=\"https://ko-fi.com/leontalon/commissions\">https://ko-fi.com/leontalon/commissions</a></p>",
    "allowNoCredit": True,
    "allowCommercialUse": [
        "Image",
        "RentCivit",
        "Rent",
        "Sell"
    ],
    "allowDerivatives": True,
    "allowDifferentLicense": True,
    "type": "LORA",
    "minor": False,
    "poi": False,
    "nsfw": False,
    "nsfwLevel": 15,
    "availability": "Public",
    "cosmetic": None,
    "supportsGeneration": True,
    "stats": {
        "downloadCount": 2051,
        "favoriteCount": 0,
        "thumbsUpCount": 385,
        "thumbsDownCount": 0,
        "commentCount": 2,
        "ratingCount": 0,
        "rating": 0,
        "tippedAmountCount": 0
    },
    "creator": {
        "username": "LeonDoesntDraw",
        "image": "https://lh3.googleusercontent.com/a/AEdFTp7zLM1fubX4omLmP2Jv6hnJw_jf7p8ANbPjEsTS=s96-c"
    },
    "tags": [
        "anime",
        "character",
        "woman",
        "girls_frontline"
    ],
    "modelVersions": [
        {
            "id": 127062,
            "index": 0,
            "name": "v2.0",
            "baseModel": "SD 1.5",
            "baseModelType": "Standard",
            "createdAt": "2023-07-27T10:36:07.312Z",
            "publishedAt": "2023-07-27T10:41:45.737Z",
            "status": "Published",
            "availability": "Public",
            "nsfwLevel": 13,
            "description": "<p>Added christmas and jacketless training</p><p>general improvements</p>",
            "trainedWords": [
                "VSKnormal",
                "VSKDress",
                "VSKJacketless",
                "VSKChristmas",
                "VSKFace"
            ],
            "covered": True,
            "stats": {
                "downloadCount": 988,
                "ratingCount": 112,
                "rating": 5,
                "thumbsUpCount": 152,
                "thumbsDownCount": 0
            },
            "files": [
                {
                    "id": 91869,
                    "sizeKB": 73888.6953125,
                    "name": "VSK.safetensors",
                    "type": "Model",
                    "pickleScanResult": "Success",
                    "pickleScanMessage": "No Pickle imports",
                    "virusScanResult": "Success",
                    "virusScanMessage": None,
                    "scannedAt": "2023-07-27T10:40:50.825Z",
                    "metadata": {
                        "format": "SafeTensor"
                    },
                    "hashes": {
                        "AutoV1": "4D71A74E",
                        "AutoV2": "260F2989F1",
                        "SHA256": "260F2989F160C67B09FD68482D1CC45DE61A33EEC5D2FA6FCD6CF7E09BBA7D47",
                        "CRC32": "93FFD3FC",
                        "BLAKE3": "253BD9C3037584A20AD46C833E9BC90A1F8F7EA031FD81BF1E8392DBC9C45F3E",
                        "AutoV3": "A799B2202ECC"
                    },
                    "downloadUrl": "https://civitai.com/api/download/models/127062",
                    "primary": True
                }
            ],
            "images": [
                {
                    "url": "https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/7e37970c-7ec7-4d61-b763-9067c7b358df/width=1024/1743604.jpeg",
                    "nsfwLevel": 4,
                    "width": 1024,
                    "height": 1416,
                    "hash": "UmJu4IWB~qt7RPayIVayskt6S5j[xZayozWV",
                    "type": "image",
                    "hasMeta": True,
                    "hasPositivePrompt": True,
                    "onSite": False,
                    "remixOfId": None
                },
                {
                    "url": "https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/f4ed7e24-edf0-4028-b59e-fea3f4061ff6/width=1024/1743620.jpeg",
                    "nsfwLevel": 1,
                    "width": 1024,
                    "height": 1416,
                    "hash": "UXHog{b_xuF~.Ts,I;TLbawIIoD*E2t6xZf7",
                    "type": "image",
                    "hasMeta": True,
                    "hasPositivePrompt": True,
                    "onSite": False,
                    "remixOfId": None
                },
                {
                    "url": "https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/1de3c46f-2d2b-4ceb-9b25-9f4ceba189ab/width=1024/1743617.jpeg",
                    "nsfwLevel": 8,
                    "width": 1024,
                    "height": 1416,
                    "hash": "UMI5[LjF6Br=.Tt60-e.4ntRxvxu={o#M}t7",
                    "type": "image",
                    "hasMeta": True,
                    "hasPositivePrompt": True,
                    "onSite": False,
                    "remixOfId": None
                },
                {
                    "url": "https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/cbe20dcf-7721-4f34-bc24-9ff14b96cab2/width=1024/1743606.jpeg",
                    "nsfwLevel": 4,
                    "width": 1024,
                    "height": 1416,
                    "hash": "U8G[{9OG9tIW6Xo#00fQ8wo09aRj00RO^%Rj",
                    "type": "image",
                    "hasMeta": True,
                    "hasPositivePrompt": True,
                    "onSite": False,
                    "remixOfId": None
                },
                {
                    "url": "https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/62a723b9-3fee-4826-9567-b3c28c678282/width=1024/1743603.jpeg",
                    "nsfwLevel": 8,
                    "width": 1024,
                    "height": 1416,
                    "hash": "USI4U}NH01WUtPRk57xZE0xajct6~VWCE2ay",
                    "type": "image",
                    "hasMeta": True,
                    "hasPositivePrompt": True,
                    "onSite": False,
                    "remixOfId": None
                },
                {
                    "url": "https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/b089d589-deca-4c4c-ab55-1d22a1aa0405/width=1024/1743601.jpeg",
                    "nsfwLevel": 8,
                    "width": 1024,
                    "height": 1416,
                    "hash": "UJIq7M~B01n$In4:9axZ-o-pE2s:9tE2ogR*",
                    "type": "image",
                    "hasMeta": True,
                    "hasPositivePrompt": True,
                    "onSite": False,
                    "remixOfId": None
                },
                {
                    "url": "https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/1833e6e8-e07e-4947-9ee8-2ff08f9aff05/width=1024/1743599.jpeg",
                    "nsfwLevel": 4,
                    "width": 1024,
                    "height": 1416,
                    "hash": "U8Jt#Y}+000000J65A-p3D%24nENDO-7KQnP",
                    "type": "image",
                    "hasMeta": True,
                    "hasPositivePrompt": True,
                    "onSite": False,
                    "remixOfId": None
                },
                {
                    "url": "https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/d3d7580e-acef-4831-a74d-f89c0e5399ed/width=1024/1743600.jpeg",
                    "nsfwLevel": 8,
                    "width": 1024,
                    "height": 1416,
                    "hash": "UKMQFs%L02t7?]jY?wxu%#j?sAs:HrkC9Fju",
                    "type": "image",
                    "hasMeta": True,
                    "hasPositivePrompt": True,
                    "onSite": False,
                    "remixOfId": None
                },
                {
                    "url": "https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/2f3e5f3c-b8f2-4e17-906f-16f6f00cc776/width=1024/1743595.jpeg",
                    "nsfwLevel": 1,
                    "width": 1024,
                    "height": 1152,
                    "hash": "URNl}S~p01tR_0WURQ%10gxvNLIoIBRjE2Rl",
                    "type": "image",
                    "hasMeta": True,
                    "hasPositivePrompt": True,
                    "onSite": False,
                    "remixOfId": None
                },
                {
                    "url": "https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/e31fe12a-7080-44c7-9254-3c7e246e7b8c/width=1024/1743596.jpeg",
                    "nsfwLevel": 1,
                    "width": 1024,
                    "height": 1152,
                    "hash": "UQNl}PNZ02t9~QogIWIo0MRPNLxaR7s.9Zxa",
                    "type": "image",
                    "hasMeta": True,
                    "hasPositivePrompt": True,
                    "onSite": False,
                    "remixOfId": None
                }
            ],
            "downloadUrl": "https://civitai.com/api/download/models/127062"
        },
        {
            "id": 13966,
            "index": 1,
            "name": "v1.0",
            "baseModel": "SD 1.5",
            "baseModelType": "Standard",
            "createdAt": "2023-02-22T18:41:53.988Z",
            "publishedAt": "2023-02-22T18:41:53.988Z",
            "status": "Published",
            "availability": "Public",
            "nsfwLevel": 11,
            "trainedWords": [
                "vsk",
                "vskdress"
            ],
            "covered": True,
            "stats": {
                "downloadCount": 1063,
                "ratingCount": 233,
                "rating": 5,
                "thumbsUpCount": 236,
                "thumbsDownCount": 0
            },
            "files": [
                {
                    "id": 12247,
                    "sizeKB": 147533.7412109375,
                    "name": "VSK.safetensors",
                    "type": "Model",
                    "pickleScanResult": "Success",
                    "pickleScanMessage": "No Pickle imports",
                    "virusScanResult": "Success",
                    "virusScanMessage": None,
                    "scannedAt": "2023-02-22T18:46:17.348Z",
                    "metadata": {
                        "format": "SafeTensor",
                        "size": "full",
                        "fp": "fp16"
                    },
                    "hashes": {
                        "AutoV1": "C7B41150",
                        "AutoV2": "5E8CA396E4",
                        "SHA256": "5E8CA396E45A596CC3F5B376B869EE4095617839B63ED2A352CAD7C9CA5712E2",
                        "CRC32": "3A1842FF",
                        "BLAKE3": "4791680017CEB2E6ADF0A7F01BADC442C95266BD8B0852F862D5675A45054769",
                        "AutoV3": "5F86F0A0EB1F"
                    },
                    "downloadUrl": "https://civitai.com/api/download/models/13966",
                    "primary": True
                }
            ],
            "images": [
                {
                    "url": "https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/650b84aa-1ed9-4a71-ff1c-8def983b9200/width=1280/135662.jpeg",
                    "nsfwLevel": 2,
                    "width": 1280,
                    "height": 1600,
                    "hash": "UgG9Q]RkIUo~~qofIqo#-;Rjt8W=tRWBtRfl",
                    "type": "image",
                    "hasMeta": True,
                    "hasPositivePrompt": True,
                    "onSite": False,
                    "remixOfId": None
                },
                {
                    "url": "https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/c2812079-ce1e-4275-6ff5-d78b8ce5f500/width=1280/135661.jpeg",
                    "nsfwLevel": 1,
                    "width": 1280,
                    "height": 1600,
                    "hash": "UXE{IS-;E1Rj~VxtIqWCoIfkozoJxZayWCof",
                    "type": "image",
                    "hasMeta": True,
                    "hasPositivePrompt": True,
                    "onSite": False,
                    "remixOfId": None
                },
                {
                    "url": "https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/358ec8e8-9256-42e3-8ce3-3646cb48d000/width=1280/135660.jpeg",
                    "nsfwLevel": 8,
                    "width": 1280,
                    "height": 1600,
                    "hash": "UBF=Eqof01OD~7NG00xt0KRj-pxaT0s:krt7",
                    "type": "image",
                    "hasMeta": True,
                    "hasPositivePrompt": True,
                    "onSite": False,
                    "remixOfId": None
                },
                {
                    "url": "https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/d1ae12bd-5b79-498d-cf5a-0aff20bc4800/width=1280/135663.jpeg",
                    "nsfwLevel": 8,
                    "width": 1280,
                    "height": 1600,
                    "hash": "UDEoJWxa01NG~URj0L%2NZt7s;NG-nRjkDof",
                    "type": "image",
                    "hasMeta": True,
                    "hasPositivePrompt": True,
                    "onSite": False,
                    "remixOfId": None
                }
            ],
            "downloadUrl": "https://civitai.com/api/download/models/13966"
        }
    ]
}

@pytest.fixture
def session():
    from os.path import dirname, join
    engine = create_engine("sqlite:///:memory:")
    # engine = create_engine(f"sqlite:///{join(dirname(__file__), 'db.sqlite3')}")
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session

def test_create_model(civitai_model_data_1, session):
    model_validate = ModelId_Response(**civitai_model_data_1)

    model_1 = CivitAI_Model(
        id=model_validate.id,
        name=model_validate.name,
        type=model_validate.type,
        nsfw=model_validate.nsfw,
        model_id_info=model_validate.model_dump(),
        tags=[],
        model_versions=[]
        )

    for version in model_validate.modelVersions:
        model_1.model_versions.append(
            CivitAI_ModelVersion(
                id=version.id,
                model_id=model_validate.id,
                model=model_1
            )
        )

    for tag in model_validate.tags:
        model_1.tags.append(CivitAI_Tag(
            name=tag
        ))

    session.add(model_1)
    session.commit()

    assert model_1.id == model_validate.id
    statement_1 = select(CivitAI_ModelVersion).where(CivitAI_ModelVersion.id == model_validate.modelVersions[0].id)
    version_result_1 = session.exec(statement_1)
    for result in version_result_1:
        if (result.id == model_validate.modelVersions[0].id):
            assert True
        else:
            raise AssertionError()

    statement_2 = select(CivitAI_Tag)
    tag_result_2 = session.exec(statement_2)
    for result in tag_result_2:
        if (result.name in model_validate.tags):
            assert True
        else:
            raise AssertionError()
    
    tag_result_2 = session.exec(statement_2).all()
    assert len(tag_result_2) == 4

    # assert model_1.json_data['id'] == model_1.id