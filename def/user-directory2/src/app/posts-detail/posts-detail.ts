import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { CommonModule } from '@angular/common';
import { PostService, Post } from '../post';

@Component({
  selector: 'app-posts-detail',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './posts-detail.html',
  styleUrl: './posts-detail.css'
})
export class PostsDetail implements OnInit {
  post: Post | null = null;

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private postService: PostService
  ) {}

  ngOnInit(): void {
    const id = Number(this.route.snapshot.paramMap.get('id'));
    this.postService.getPost(id).subscribe(data => {
      this.post = data;
    });
  }

  goBack(): void {
    this.router.navigate(['/posts']);
  }
}