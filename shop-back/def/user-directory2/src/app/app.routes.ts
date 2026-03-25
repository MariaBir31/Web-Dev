import { Routes } from '@angular/router';
import { Home } from './home/home';
import { Posts } from './posts/posts';
import { PostsDetail } from './posts-detail/posts-detail';

export const routes: Routes = [
  { path: '', redirectTo: 'home', pathMatch: 'full' },
  { path: 'home', component: Home },
  { path: 'posts', component: Posts },
  { path: 'posts/:id', component: PostsDetail }
];

