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
  // createdAt: 'string', //ISO 8061 // 这个并没有出现在 models endpoint，嘻嘻civitai里这帮逆天程序员写的什么几把东西？这么多对象不一致的问题存在，有没有调用过自己写的API？
  downloadUrl: 'string.url',
  files: modelVersion_Base_file.array(),
  images: modelVersion_Base_image.array(),
})
