import { Injectable } from "@angular/core";
import { EntityState, EntityStore, StoreConfig } from "@datorama/akita";
import { Request } from "./request.model";

export interface RequestsState extends EntityState<Request> {}

@Injectable({ providedIn: "root" })
@StoreConfig({ name: "requests" })
export class RequestsStore extends EntityStore<RequestsState> {

  constructor() {
    super();
  }

}
