import { Injectable } from "@angular/core";
import { QueryEntity } from "@datorama/akita";
import { RequestsStore, RequestsState } from "./requests.store";

@Injectable({ providedIn: "root" })
export class RequestsQuery extends QueryEntity<RequestsState> {

  constructor(protected store: RequestsStore) {
    super(store);
  }

}
