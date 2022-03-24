import { Injectable } from "@angular/core";
import { EntityState, EntityStore, StoreConfig } from "@datorama/akita";
import { Role } from "./role.model";

export interface RolesState extends EntityState<Role> {}

@Injectable({ providedIn: "root" })
@StoreConfig({ name: "roles" })
export class RolesStore extends EntityStore<RolesState> {

  constructor() {
    super();
  }

}
