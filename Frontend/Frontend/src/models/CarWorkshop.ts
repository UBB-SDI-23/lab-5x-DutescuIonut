import { CarTunedBy } from "./CarTunedBy";

export interface CarWorkshop{
    id:number;
    Name:string;
    Owner:string;
    Founded:number;
    Location:string;
    NumberOfEmployees:number;
    // carsTuned:string;
    carsTuned:CarTunedBy[];
}