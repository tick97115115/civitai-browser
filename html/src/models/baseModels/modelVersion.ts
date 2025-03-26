import { type } from 'arktype'
import { modelVersion_Base_file, modelVersion_Base_image } from './misc'

// https://www.jsondiff.com/ 找到共有属性名

export const modelVersion_Base = type({
  id: 'number',
  name: 'string',
  publishedAt: 'string', // ISO 8061
  // status: 'string',
  trainedWords: 'string[]',
  baseModel: 'string',
  // createdAt: 'string', //ISO 8061 // 这个并没有出现在 models endpoint
  downloadUrl: 'string.url',
  files: modelVersion_Base_file.array(),
  images: modelVersion_Base_image.array(),
})
