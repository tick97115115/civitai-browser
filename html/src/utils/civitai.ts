import { models_request_opts, models_response } from '../models/models_deprecated'
import type { ModelsRequestOpts } from '../models/models_deprecated'
import ky from 'ky'
import { objectToQueryString } from './misc'

const API_URL_V1_Creators = new URL('https://civitai.com/api/v1/creators')
const API_URL_V1_Images = new URL('https://civitai.com/api/v1/images') // https://civitai.com/api/v1/images
const API_URL_V1_Models = new URL('https://civitai.com/api/v1/models') // https://civitai.com/api/v1/models
const API_URL_V1_Model_By_Id = new URL('https://civitai.com/api/v1/models/modelId') // "https://civitai.com/api/v1/models/:modelId"
// const API_URL_ModelVersion_By_VersionId = urljoin(API_URL_V1, "model-versions/")  // "https://civitai.com/api/v1/model-versions/:modelVersionId"
// const API_URL_ModelVersion_By_Hash = urljoin(API_URL_V1, "model-versions/by-hash/") // "https://civitai.com/api/v1/model-versions/by-hash/:hash"
const API_URL_Tags = new URL('https://civitai.com/api/v1/tags') // https://civitai.com/api/v1/tags

async function models(params: ModelsRequestOpts) {
  const res = await ky.get(API_URL_V1_Models, { searchParams: objectToQueryString(params) })
}
