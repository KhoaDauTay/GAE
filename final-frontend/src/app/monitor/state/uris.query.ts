import { Injectable } from "@angular/core";
import { QueryEntity } from "@datorama/akita";
import { UrisStore, UrisState } from "./uris.store";

@Injectable({ providedIn: "root" })
export class UrisQuery extends QueryEntity<UrisState> {

  constructor(protected store: UrisStore) {
    super(store);
  }

}
