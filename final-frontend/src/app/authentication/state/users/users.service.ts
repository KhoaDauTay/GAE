import { Injectable } from "@angular/core";
import { NgEntityService } from "@datorama/akita-ng-entity-service";
import { UsersStore, UsersState } from "./users.store";

@Injectable({ providedIn: "root" })
export class UsersService extends NgEntityService<UsersState> {

  constructor(protected store: UsersStore) {
    super(store);
  }

}
