import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { CommonModule } from '@angular/common';
import { PostService, Post } from '../post';

@Component({
  selector: 'app-posts',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './posts.html',
  styleUrl: './posts.css'
})
export class Posts implements OnInit {
  posts: Post[] = [];
  loading = true;

  constructor(private postService: PostService, private router: Router) {}

  ngOnInit(): void {
    this.postService.getPosts().subscribe((data: Post[]) => {
      this.posts = data.slice(0, 20);
      this.loading = false;
    });
  }

  goToPost(id: number): void {
    this.router.navigate(['/posts', id]);
  }
}