import { Injectable } from "@angular/core";
import { NgEntityService } from "@datorama/akita-ng-entity-service";
import { UrisStore, UrisState } from "./uris.store";

@Injectable({ providedIn: "root" })
export class UrisService extends NgEntityService<UrisState> {

  constructor(protected store: UrisStore) {
    super(store);
  }

}
