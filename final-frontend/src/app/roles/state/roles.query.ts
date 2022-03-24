import { Injectable } from "@angular/core";
import { QueryEntity } from "@datorama/akita";
import { RolesStore, RolesState } from "./roles.store";

@Injectable({ providedIn: "root" })
export class RolesQuery extends QueryEntity<RolesState> {

  constructor(protected store: RolesStore) {
    super(store);
  }

}
