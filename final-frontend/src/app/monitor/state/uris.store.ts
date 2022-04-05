import { Injectable } from "@angular/core";
import { EntityState, EntityStore, StoreConfig } from "@datorama/akita";
import { Uris } from "./uris.model";

export interface UrisState extends EntityState<Uris> {}

@Injectable({ providedIn: "root" })
@StoreConfig({ name: "uris" })
export class UrisStore extends EntityStore<UrisState> {

  constructor() {
    super();
  }

}
