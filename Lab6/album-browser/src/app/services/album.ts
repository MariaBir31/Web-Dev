import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Album, Photo } from '../models/album.model';

@Injectable({
  providedIn: 'root'
})
export class AlbumService {

  private API_URL = 'https://jsonplaceholder.typicode.com';

  constructor(private http: HttpClient) {}

  getAlbums(): Observable<Album[]> {
    return this.http.get<Album[]>(`${this.API_URL}/albums`);
  }

  getAlbum(id: number): Observable<Album> {
    return this.http.get<Album>(`${this.API_URL}/albums/${id}`);
  }

  deleteAlbum(id: number): Observable<any> {
    return this.http.delete(`${this.API_URL}/albums/${id}`);
  }

  updateAlbum(album: Album): Observable<Album> {
    return this.http.put<Album>(`${this.API_URL}/albums/${album.id}`, album);
  }

  getAlbumPhotos(id: number): Observable<Photo[]> {
    return this.http.get<Photo[]>(`${this.API_URL}/albums/${id}/photos`);
  }

}