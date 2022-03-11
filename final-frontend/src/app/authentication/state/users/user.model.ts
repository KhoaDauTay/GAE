export interface User {
  id: string,
  name: string,
  email: string,
  role: string,
  first_name: string,
  last_name: string,
  avatar: string
  client?: {
    address: string,
    city: string,
    country: string,
    about_me: string,
    postal_code: string
  }
}

// export function createUser(params: Partial<User>) {
//   return {
//
//   } as User;
// }
