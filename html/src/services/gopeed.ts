import { Client } from '@gopeed/rest'
import { type } from 'arktype'

let connectivity = type("'connected' | 'disconnected'")
type Connectivity = typeof connectivity.infer

class GopeedService {
  gopeedClient: Client | undefined

  init(host: string, token: string = ''): void {
    this.gopeedClient = new Client({ host, token })
  }

  connectivity = connectivity('disconnected')

  async testConnection(): Promise<Connectivity> {
    if (!this.gopeedClient) {
      this.connectivity = 'disconnected'
    }
    try {
      await this.gopeedClient?.getTasks()
      this.connectivity = 'connected'
    } catch (error) {
      this.connectivity = 'disconnected'
    }
    return this.connectivity
  }
}
