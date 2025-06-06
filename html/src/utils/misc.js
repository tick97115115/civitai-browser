import { ar } from 'vuetify/locale'

/**
 * Convert any object to URLSearchParams type.
 * @param {*} obj - the object you want to process
 * @returns {URLSearchParams}
 */
export function objectToQueryString(obj) {
  const params = new URLSearchParams()

  function encode(key, value) {
    //     // 如果是数组，将每个元素作为单独的键值对添加
    if (Array.isArray(value)) {
      value.forEach((item) => params.append(`${key}[]`, item))
    } else {
      //     // 如果不是数组，直接添加
      params.append(key, value)
    }
  }

  // // 遍历对象
  Object.entries(obj).forEach(([key, value]) => {
    encode(key, value)
  })

  return params
}

// const params = {
//   page: 1,
//   limit: 10,
//   tags: ['javascript', 'web', 'api'], // 数组属性
// };

// const query = objectToQueryString(params);

// console.log(query.toString());
// // 输出: page=1&limit=10&tags[]=javascript&tags[]=web&tags[]=api

/**
 * Convert any arktype string enum to Array<string>.
 * @param {*} arktype_obj - the object you want to process
 * @returns {Array<string>}
 */
export function convert_arktype_enum_to_array(arktype_obj) {
  const raw_data = arktype_obj.toJSON()
  const arr = []
  for (let index = 0; index < raw_data.length; index++) {
    const element = raw_data[index]
    arr.push(element['unit'])
  }
  return arr
}
