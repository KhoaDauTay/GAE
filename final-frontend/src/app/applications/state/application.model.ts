export interface Application {
  id: number;
  client_id: string;
  redirect_uris: string;
  client_type: string;
  authorization_grant_type: string;
  client_secret: string;
  name: string;
  skip_authorization: boolean;
  algorithm: string;
  scopes: [];
  user?: string;
}
