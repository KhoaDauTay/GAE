import { Injectable } from "@angular/core";
import { NgEntityService } from "@datorama/akita-ng-entity-service";
import { RolesStore, RolesState } from "./roles.store";

@Injectable({ providedIn: "root" })
export class RolesService extends NgEntityService<RolesState> {

  constructor(protected store: RolesStore) {
    super(store);
  }

}
