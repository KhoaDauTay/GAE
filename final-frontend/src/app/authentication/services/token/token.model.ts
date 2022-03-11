export interface Tokens {
  access: string;
  refresh: string;
}

export interface JwtPayload {
  iat?: number;
  exp?: number;
  jti?: string;
  user_id: number;
  role: string
}
