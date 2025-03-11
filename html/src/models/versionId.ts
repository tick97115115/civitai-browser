import { type } from 'arktype'

const versionId_response_file_hashes = type({
  SHA256: 'string',
  CRC32: 'string',
  BLAKE3: 'string',
  AutoV3: 'string',
})

const versionId_response_files = type([
  {
    name: 'string',
    id: 'number.integer',
    sizeKb: 'number',
    'metadata?': {
      fp: '"fp8" | "fp16" | "fp32"',
      size: '"full" | "pruned"',
      format: '"SafeTensor" | "PickleTensor" | "Other" | "Diffusers"',
    },
    pickleScanResult: '"Pending" | "Success" | "Danger" | "Error"',
    virusScanResult: '"Pending" | "Success" | "Danger" | "Error"',
    'scannedAt?': 'string',
    hashes: versionId_response_file_hashes,
    downloadUrl: 'string.url',
    'primary?': 'boolean',
  },
])

const versionId_response_images = type([
  {
    url: 'string.url',
    nsfwLevel: 'number.integer',
    width: 'number.integer',
    height: 'number.integer',
    hash: 'string',
    'meta?': {
      ENSD: 'string',
      Size: 'string',
      seed: 'number.integer',
      Score: 'string',
      steps: 'number.integer',
      prompt: 'string',
      sampler: 'string',
      'Eta DDIM': 'string',
      cfgScale: 'number',
      // resources: '[]'
      'Model hash': 'string',
      'Hires upscale': 'string',
      'Hires upscaler': 'string',
      negativePrompt: 'string',
      'Denoising strength': 'string',
    },
  },
])

export const versionId_response = type({
  id: 'number.integer',
  baseModel: 'string',
  name: 'string',
  'createdAt?': 'string.date',
  'updatedAt?': 'string.date',
  publishedAt: 'string.date',
  downloadUrl: 'string.url',
  files: versionId_response_files,
  images: versionId_response_images,
  state: {
    downloadCount: 'number.integer',
    ratingCont: 'number.integer',
    rating: 'number',
  },
})
