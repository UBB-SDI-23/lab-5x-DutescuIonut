import { CarBrand } from "./CarBrand";
import { CarTunedBy } from "./CarTunedBy";
import { Owner } from "./Owner";

export interface Car
{

    id:number;
    CarBrand:CarBrand;//...
    CarModel:string;
    ProductionYear:number;
    SeatsNumber:number;
    Color:string;
    OwnerCNP:Owner;//...
    workshops:CarTunedBy[];
    // workshops:string;
}