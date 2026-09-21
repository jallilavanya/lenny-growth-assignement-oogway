export type Session={id:string;title:string;created_at:string;updated_at:string};
export type Source={title:string;episode:string;source_url:string;chunk_id:string;relevance:number};
export type Message={id:string;role:string;content:string;created_at:string;metadata?:{sources?:Source[]}};
