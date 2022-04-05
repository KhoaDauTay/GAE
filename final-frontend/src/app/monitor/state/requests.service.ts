import { Injectable } from "@angular/core";
import { NgEntityService } from "@datorama/akita-ng-entity-service";
import { RequestsStore, RequestsState } from "./requests.store";

@Injectable({ providedIn: "root" })
export class RequestsService extends NgEntityService<RequestsState> {

  constructor(protected store: RequestsStore) {
    super(store);
  }

}
