export interface ProductType {
  id: number;
  media: string;
  title: string;
  description: string;
  price: number;
  oldPrice?: number;
  isNew: boolean;
  quantity: number;
}
