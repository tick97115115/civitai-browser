import { type } from 'arktype'

// https://www.jsondiff.com/ 找到共有属性名

export const model_types = type(
  "'Checkpoint' | 'TextualInversion' | 'Hypernetwork' | 'AestheticGradient' | 'LORA' | 'Controlnet' | 'Poses' | 'LoCon' | 'DoRA' | 'Other' | 'MotionModule' | 'Upscaler' | 'VAE' | 'Wildcards' | 'Workflows' | 'Detection'",
)
export const models_request_period = type("'AllTime' | 'Day' | 'Week' | 'Month' | 'Year'")
export const allowCommercialUse = type("'Image' | 'RentCivit' | 'Rent' | 'Sell' | 'None'")
export const models_request_sort = type("'Highest Rated' | 'Most Downloaded' | 'Newest'")

export const nsfwLevel = type("'None' | 'Soft' | 'Mature' | 'X'")
export const modelVersion_Base_hashes = type({
  'SHA256?': 'string',
  'CRC32?': 'string',
  'BLAKE3?': 'string',
  'AutoV3?': 'string',
  'AutoV2?': 'string',
  'AutoV1?': 'string',
})

export const modelVersion_Base_file = type({
  name: 'string',
  id: 'number.integer',
  'metadata?': {
    //   fp: '"fp8" | "fp16" | "fp32"',
    //   size: '"full" | "pruned"',
    // 'format?': '"SafeTensor" | "PickleTensor" | "Other" | "Diffusers" | "GGUF"',
  },
  pickleScanResult: '"Pending" | "Success" | "Danger" | "Error"',
  virusScanResult: '"Pending" | "Success" | "Danger" | "Error"',
  // primary: 'boolean',
  scannedAt: 'string', //ISO 8061
  type: 'string',
  hashes: modelVersion_Base_hashes,
  downloadUrl: 'string.url',
})

export const modelVersion_Base_image = type({
  url: 'string.url',
  nsfwLevel: 'number.integer',
  width: 'number.integer',
  height: 'number.integer',
  hash: 'string',
  // meta: {} too unstructured
})
